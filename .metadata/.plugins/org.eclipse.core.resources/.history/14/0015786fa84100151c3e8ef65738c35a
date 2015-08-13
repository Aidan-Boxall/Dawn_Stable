import scisoftpy as dnp
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
import finding_the_rotation_matrix as rm
import copy
import scitbx.math as scm
from scitbx.matrix import col as Vector
from scitbx.matrix import sqr as Rotator
from itertools import permutations
import time

def arccos(x):
    if x < -1:
        return dnp.arccos(-1)
    if x >  1:
        return dnp.arccos(1)
    else:
        return dnp.arccos(x)

def add_rot_error(vector):
    stddev = 0.1
#             rand_rotation_x = rm.Rotator(rm.Vector(1),stddev)#,dnp.ranom.normal(0,stddev))
#             rand_rotation_y = rm.Rotator(rm.Vector(0,1),-stddev)#, dnp.random.normal(0,stddev))
#             rand_rotation_z = rm.Rotator(rm.Vector(0,0,1),stddev)#,dnp.random.normal(0,stddev))
    rand_axis = Vector([dnp.random.random(),dnp.random.random(),dnp.random.random()])
    rand_rotation = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(rand_axis, stddev, deg=True))
    vector = rand_rotation * vector
    return vector

def random_rotation():
    rand_rotation_x = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(Vector([1.0,0,0]) ,dnp.random.randint(0,361), deg=True))
    rand_rotation_y = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(Vector([0,1.0,0]),dnp.random.randint(0,361), deg=True))
    rand_rotation_z = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(Vector([0.0,0.0,1.0]),dnp.random.randint(0,361), deg=True))
    return rand_rotation_z*rand_rotation_y*rand_rotation_x


def diff(U, data, vectors):
        """This is a function used to optimise the U matrix. It evaluates
        """
        data = rm.rotate_list(U, data)
        index_list=[]
        for i, dat in enumerate(data):
            diffs = []
            dat = dat
            for j, vector in enumerate(vectors):
                diffs.append((dat-vector).length())
            index = diffs.index(min(dnp.abs(diffs)))
            index_list.append(index)
        targets = [0]*len(data)
        for i, idx in enumerate(index_list):
            targets[i] = vectors[idx]
        total = 0
        for i, dat in enumerate(data):
            total += (dat - targets[i]).length()
        return total


def test_data(mock_data, all_vectors_rot, all_vectors, mycrys, old_filter, vectors=False, fig=None):
    if not old_filter:
        U = rm.find_U_matrix(mock_data, mycrys)
    else:
        U = rm.find_U_matrix(mock_data, mycrys, refl='allowed')

    difference = diff(U, all_vectors_rot, all_vectors)

    print 'diff', difference

    fig = plt.figure()

    ax = fig.add_subplot(311, projection='3d')
    ax.set_title('Unedited Reciprocal Space')
    f.plot_vectors(all_vectors, fig, ax)

    ax = fig.add_subplot(312, projection='3d')
    ax.set_title('Randomly Rotated Reciprocal Space')
    f.plot_vectors(all_vectors_rot, fig, ax)

    all_vectors_rot = rm.rotate(U, all_vectors_rot)

    ax = fig.add_subplot(313, projection='3d')
    ax.set_title('Randomly Rotated Reciprocal Space after U Matrix')
    f.plot_vectors(all_vectors_rot, fig, ax)

    f.plot_vectors(all_vectors)
    f.plot_vectors(rm.rotate_list(U, all_vectors_rot))

    if vectors is not False:
        fig = plt.figure()
        ax = fig.add_subplot(311, projection='3d')
        ax.set_title('Vectors Before Rotation')
        f.plot_vectors(vectors, fig, ax)
        f.plot_sphere(vectors[0].length(), fig, ax)

        ax = fig.add_subplot(312, projection='3d')
        ax.set_title('Mock Data')
        f.plot_vectors(mock_data, fig, ax)
        f.plot_sphere(mock_data[0].length(), fig, ax)

        mock_data = rm.rotate_list(U, mock_data)

        ax = fig.add_subplot(313, projection='3d')
        ax.set_title('Mock Data after U Matrix')
        f.plot_vectors(mock_data, fig, ax)
        f.plot_sphere(mock_data[0].length(), fig, ax)

    if difference < 5:
        return True
    else:
        return False


def test_by_hkl(cif, hkl_list, add_error=False, old_filter=False):
    mycrys = c.Crystal()
    mycrys.load_cif(cif)
    if old_filter:
        refl = 'allowed'
    else:
        refl = 'orient'
    grouped_reflections = group_reflections(mycrys, energy=energy, refl=refl)
    all_vectors_hkl = []
    all_vectors = []
    for i, group in enumerate(grouped_reflections):
        group_vectors = momentum_transfer_vectors(group, mycrys)
        for j, item in enumerate(group):
            vector_hkl = (group_vectors[j], item[0])
            all_vectors_hkl.append(vector_hkl)
            all_vectors.apped(group_vectors[j])
    vectors = []
    for hkl in hkl_list:
        for vector in all_vectors_hkl:
            if hkl == vector[1]:
                vectors.append(vector[0])
                break
    rand_rotation = random_rotation()
    mock_data = rm.rotate_list(rand_rotation, vectors)
    all_vectors_rot = rm.rotate_list(rand_rotation, all_vectors)
    if add_error:
        mock_data = [add_rot_error(dat) for dat in mock_data]
    if test_data(mock_data, all_vectors_rot, all_vectors, mycrys, old_filter, vectors):
        return True
    else:
        return False

cif = 'Hexagonal.cif'
hkl_list = [ (-1, 2, 0), (2, -1, 0), (-1, -1, 0)]
test_by_hkl(cif, hkl_list, add_error=False, old_filter=False)
plt.show