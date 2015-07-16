import scisoftpy as dnp
import copy
import scitbx.math as scm
from scitbx.matrix import col as Vector
from scitbx.matrix import sqr as Rotator


def combinations(iterable, r):
    """Equivalent to itetools.combinations which is not available in jython"""
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def get_rotator(vector, target):
    """Given a vector and a target vector finds the Rotator that turns one into
    the other.
    """
    axis = vector.cross(target)
    axis = axis.normalize()
    angle = dnp.arccos(vector.normalize().dot(target.normalize()))
    return Rotator(scm.r3_rotation_axis_and_angle_as_matrix(axis, angle))


def get_second_rotator(origional_target, vector, target):
    axis = origional_target.normalize()
#     axis = Vector(0,0,1)
    vector = vector.normalize()
    target = target.normalize()
    v1 = vector - axis*(vector.dot(axis))
    v2 = target - axis*(target.dot(axis))
    angle = dnp.arccos(v1.normalize().dot(v2.normalize()))
    angle = float(angle)
    if (v1.cross(v2)).length()<10**-15:
        raise Exception('vector and target are parallel so the cross product is zero')
    if ((v1.cross(v2)).normalize()).dot(axis.normalize()) > 0:
        return Rotator(scm.r3_rotation_axis_and_angle_as_matrix(axis, angle))
    else:
        return Rotator(scm.r3_rotation_axis_and_angle_as_matrix(axis, -angle))

def finding_the_targets(found_vectors, theoretical_vectors):
    if len(found_vectors) == 2:
        found_dot = (found_vectors[0].normalize()).dot(found_vectors[1].normalize())
        found_angle = float(dnp.rad2deg(dnp.arccos(found_dot)))
        for r in range(9, 1, -1):
            # Filter by length:
            correct_length = []
            for vector in theoretical_vectors:
                for found_vector in found_vectors:
                    if round(vector.length(), r) == round(found_vector.length(), r):
                        correct_length.append(vector)
                        break
            for combination in combinations(correct_length, 2):
                if round(combination[0].length(), r) == round(
                    found_vectors[0].length(), r) and round(combination[1].length(),
                        r) == round(found_vectors[1].length(), r):
                    target_dot = (combination[0].normalize()).dot(combination[1].normalize())
                    target_angle = float(dnp.rad2deg(dnp.arccos(target_dot)))
                    if found_angle-0.5 < target_angle < found_angle+0.5:
                        return list(combination)
                if round(combination[0].length(), r) == round(
                    found_vectors[1].length(), r) and round(combination[1].length(),
                        r) == round(found_vectors[0].length(), r): 
                    target_dot = combination[0].normalize().dot(combination[1].normalize())
                    target_angle = float(dnp.rad2deg(dnp.arccos(target_dot)))
                    if found_angle-0.5 < target_angle < found_angle+0.5:
                        return [combination[1], combination[0]]
        raise Exception("""Could not find two vectors with moduli that match the
                            theoretical vectors to an accuracy of 2 decimal
                                places and an angle between them which matches to 
                                    the nearest degree.""")
    else:


        def check_third_vector(targets, found_vectors, correct_length):
            M = scm.matrix.sqr(found_vectors[0].elems + found_vectors[1].elems + found_vectors[2].elems)
            if dnp.abs(M.determinant())<10**-3:
                # Vectors are coplanar so cannot use cross product method but can use angles alone.
                # find third targets
                dot0 = found_vectors[0].normalize().dot(found_vectors[2].normalize())
                dot1 = found_vectors[1].normalize().dot(found_vectors[2].normalize())
                angle0 = float(dnp.rad2deg(dnp.arccos(dot0)))
                angle1 = float(dnp.rad2deg(dnp.arccos(dot1)))
                found_plane_normal = (found_vectors[0].cross(found_vectors[1])).normalize()
                cross0 = (found_vectors[0].cross(found_vectors[2])).normalize()
                cross1 = (found_vectors[1].cross(found_vectors[2])).normalize()
                norm_proj0 = cross0.dot(found_plane_normal)
                norm_proj1 = cross1.dot(found_plane_normal)
                for vector in correct_length:
                    if vector != targets[0] and vector != targets[1]:
                        t_dot0 = targets[0].normalize().dot(vector.normalize())
                        t_angle0 = float(dnp.rad2deg(dnp.arccos(t_dot0)))
                        t_dot1 = targets[1].normalize().dot(vector.normalize())
                        t_angle1 = float(dnp.rad2deg(dnp.arccos(t_dot1)))
                        if angle0-0.5 <t_angle0 < angle0+0.5 and angle1-0.5 <t_angle1 < angle1+0.5:
                            target_plane_normal = (targets[0].cross(targets[1])).normalize()
                            t_cross0 = (targets[0].cross(vector)).normalize()
                            t_cross1 = (targets[1].cross(vector)).normalize()
                            t_norm_proj0 = t_cross0.dot(target_plane_normal)
                            t_norm_proj1 = t_cross1.dot(target_plane_normal)
                            if t_norm_proj0 < 0 and norm_proj0 < 0 or t_norm_proj0 > 0 and norm_proj0 > 0:
                                if t_norm_proj1 < 0 and norm_proj1 < 0 or t_norm_proj1 > 0 and norm_proj1 > 0:
                                    return targets
                return [] # Reset targets as wrong combination was found
            else:
                target_plane_normal = (targets[0].cross(targets[1])).normalize()
                found_plane_normal = (found_vectors[0].cross(found_vectors[1])).normalize()
                found_dot = found_vectors[2].normalize().dot(found_plane_normal)
                # find third target
                dot0 = found_vectors[0].normalize().dot(found_vectors[2].normalize())
                dot1 = found_vectors[1].normalize().dot(found_vectors[2].normalize())
                angle0 = float(dnp.rad2deg(dnp.arccos(dot0)))
                angle1 = float(dnp.rad2deg(dnp.arccos(dot1)))
                for vector in correct_length:
                    if vector != targets[0] and vector != targets[1]:
                        t_dot0 = targets[0].normalize().dot(vector.normalize())
                        t_angle0 = float(dnp.rad2deg(dnp.arccos(t_dot0)))
                        t_dot1 = targets[1].normalize().dot(vector.normalize())
                        t_angle1 = float(dnp.rad2deg(dnp.arccos(t_dot1)))
                        if angle0-0.5 <t_angle0 < angle0+0.5 and angle1-0.5 <t_angle1 < angle1+0.5:
                            target_dot = vector.normalize().dot(target_plane_normal)
                            if target_dot < 0 and found_dot < 0 or target_dot > 0 and found_dot > 0:
                                return targets
                return [] # Reset targets as wrong combination was found


        found_dot = (found_vectors[0].normalize()).dot(found_vectors[1].normalize())
        found_angle = float(dnp.rad2deg(dnp.arccos(found_dot)))
        targets = []
        for r in range(9, 1, -1):
            # Filter by length:
            correct_length = []
            for vector in theoretical_vectors:
                for found_vector in found_vectors:
                    if round(vector.length(), r) == round(found_vector.length(), r):
                        correct_length.append(vector)
                        break
            for combination in combinations(correct_length, 2):
                if combination[0] != combination[1]:
                    if round(combination[0].length(), r) == round(
                        found_vectors[0].length(), r) and round(combination[1].length(),
                            r) == round(found_vectors[1].length(), r):
                        target_dot = (combination[0].normalize()).dot(combination[1].normalize())
                        target_angle = float(dnp.rad2deg(dnp.arccos(target_dot)))
                        if found_angle-0.5 < target_angle < found_angle+0.5:
                            targets = list(combination)
                    if len(targets) == 2:
                        targets = check_third_vector(targets, found_vectors, correct_length)
                        if len(targets) == 2:
                            return targets
                    if round(combination[0].length(), r) == round(
                        found_vectors[1].length(), r) and round(combination[1].length(),
                            r) == round(found_vectors[0].length(), r): 
                        target_dot = combination[0].normalize().dot(combination[1].normalize())
                        target_angle = float(dnp.rad2deg(dnp.arccos(target_dot)))
                        if found_angle-0.5 < target_angle < found_angle+0.5:
                            targets = [combination[1], combination[0]]
                    if len(targets) == 2:
                        targets = check_third_vector(targets, found_vectors, correct_length)
                        if len(targets) == 2:
                            return targets
        raise Exception("""Could not find two vectors with moduli that match the
                                theoretical vectors to an accuracy of 2 decimal
                                    places and an angle between them which matches to 
                                        the nearest degree.""")

def rotate_list(rotation, vector_list):
    vectors_list = copy.deepcopy(vector_list)
    for i, vector in enumerate(vectors_list):
        vector = rotation * vector
        vectors_list[i] = vector
    return vectors_list

# def get_third_rotator(origional_target, vector, target):
#     axis = origional_target
#     axis = axis.normalize()
#     vector = vector.normalize()
#     target = target.normalize()
#     v1 = vector - (vector*axis)*axis
#     v2 = target - (target*axis)*axis
#     print (vector*axis)*axis, (target*axis)*axis
#     angle = dnp.arccos(v1*v2)
#     angle = float(dnp.rad2deg(angle))
#     return Rotator(axis,-angle)


# x =Vector()
# y = Vector(0,1)
# print x
# y = y.normalize()
# z = Vector(0,0,1)
# # z = Vector(0,0,5)
# # r = Rotator(z,90)
# r = get_rotator(x,y)
# # z = r*x
# print r.R
# print y,z
# m = Rotator(z,90)
# n =m*m
# print n.R
# y = m*y
# print y



