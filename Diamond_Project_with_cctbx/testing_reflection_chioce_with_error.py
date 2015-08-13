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


def test_data(mock_data, all_vectors_rot, all_vectors, mycrys,i,j,k, old_filter, vectors=False, fig=None):
    if not old_filter:
        U = rm.find_U_matrix(mock_data, mycrys)
    else:
        U = rm.find_U_matrix(mock_data, mycrys, refl='allowed')
    difference = diff(U, all_vectors_rot, all_vectors)
    final_vectors = rm.rotate_list(U, all_vectors_rot)
#     ax = fig.add_subplot(313, projection='3d')
#     f.plot_vectors(final_vectors, fig, ax)
    print
    print
    print 'diff', difference
    log = open('test_log_with_error.txt', 'a')
    log.write('Difference: '+str(difference))
    log.write('\n')
    log.close()
    if difference < 5:
        if old_filter:
            log = open('test_log_with_error.txt', 'a')
            log.write('OLD FILTER: CASE PASSED')
            log.write('\n \n')
            log.close()
        else:
            log = open('test_log_with_error.txt', 'a')
            log.write('NEW FILTER: CASE PASSED')
            log.write('\n \n')
            log.close()
        return True
    else:
#         if vectors is not False:
#             fig = plt.figure()
#             ax = fig.add_subplot(111, projection='3d')
#             f.plot_vectors(vectors, fig, ax)
#             f.plot_sphere(vectors[0].length(), fig, ax)
#         fig = plt.figure()
#         ax = fig.add_subplot(311, projection='3d')
#          
#         f.plot_vectors(mock_data, fig, ax)
#         f.plot_sphere(mock_data[0].length(), fig, ax)
#         ax = fig.add_subplot(312, projection='3d')
#          
#         mock_data = rm.rotate_list(U, mock_data)
#         f.plot_vectors(mock_data, fig, ax)
#         f.plot_sphere(mock_data[0].length(), fig, ax)
#          
#         ax = fig.add_subplot(313, projection='3d')
#         f.plot_vectors([vectors[i], vectors[j], vectors[k]], fig, ax)
#         f.plot_sphere(mock_data[0].length(), fig, ax)
#          
#         f.plot_vectors(all_vectors)
#         f.plot_vectors(rm.rotate_list(U, all_vectors_rot))
#         plt.show()
        if old_filter:
            log = open('test_log_with_error.txt', 'a')
            log.write('OLD FILTER: CASE FAILLED')
            log.write('\n \n')
            log.close()
        else:
            log = open('test_log_with_error.txt', 'a')
            log.write('NEW FILTER: CASE FAILLED')
            log.write('\n \n')
            log.close()
        return False

def test_at_random(cif_list, old_filter=False):
    l = []
    i = 0
    j = i
    k = i
    print 'Choosing a cif file...'
    while len(l) < 2:
        mycrys = c.Crystal()
        cif_indx = dnp.random.randint(len(cif_list))
        cif = cif_list[cif_indx]
        mycrys.load_cif(cif)
        if old_filter:
            l = f.group_reflections(mycrys, refl = 'allowed')
        else:
            l = f.group_reflections(mycrys)
            if len(l)==0:
                print 'Chose {0}'.format(cif)
                print 'NEW FILTER: CASE FAILLED DUE TO NO REFLECITONS GETTING THROUGH FILTER'
                print
                print
                log = open('test_log_with_error.txt', 'a')
                log.write('Chose {0}'.format(cif)+'\n')
                log.write('NEW FILTER: CASE FAILLED DUE TO NO REFLECITONS GETTING THROUGH FILTER')
                log.write('\n \n')
                log.close()
                del cif_list[cif_indx]
                return cif_list
        new_l = []
        for old_l in l:
            if len(old_l) > 2:
                new_l.append(old_l)
        l = new_l


    print 'Chose {0} now creating list of all vectors...'.format(cif)
    log = open('test_log_with_error.txt', 'a')
    log.write('Chose cif file: {0}'.format(cif))
    log.write('\n \n')
    log.close()
    all_vectors = []
    for i, group in enumerate(l):
        all_g = f.momentum_transfer_vectors(group, mycrys)
        all_vectors += all_g
#     fig = plt.figure()
#     ax = fig.add_subplot(311, projection='3d')
#     f.plot_vectors(all_vectors, fig, ax)
    print 'Created list of all vectors and it contains {0} vectors,  now choosing reflections...'.format(len(all_vectors))
    mock_data = []
    while mock_data == []:
        if len(l) == 0:
            log = open('test_log_with_error.txt', 'a')
            log.write("Couldn't find a good set of reflections so starting again...")
            log.write('\n \n')
            log.close()
            print "Couldn't find a good set of reflections so starting again..."
            return 'Start over'
        l_index = dnp.random.randint(len(l))
        vectors = f.momentum_transfer_vectors(l[l_index], mycrys)
        combos = []
        for permutation in permutations(range(len(vectors)), 3):
            combos.append(permutation)
        dot = 0
        while dot<10**(-5) or 179.5<dot<180.5:
            if len(combos) == 0:
                del l[l_index]
                mock_data = []
                break
            indx = dnp.random.randint(len(combos))
            i, j, k = combos[indx]
            del combos[indx]
            dot = dnp.rad2deg(arccos(vectors[i].normalize().dot(vectors[j].normalize())))
            if dnp.abs(180-dnp.rad2deg(arccos(vectors[k].normalize().dot(vectors[i].normalize()))))%180.0 < 1:
                dot = 0
            elif dnp.abs(180-dnp.rad2deg(arccos(vectors[k].normalize().dot(vectors[j].normalize()))))%180.0 < 1:
                dot = 0
            mock_data = [vectors[i], vectors[j], vectors[k]]
            if len(combos) == 0 and dot<10**(-5) or 179.5<dot<180.5:
                del l[l_index]
                mock_data = []
                break
    print i, j, k , l_index, len(l)
    log = open('test_log_with_error.txt', 'a')
    log.write('Chose reflections {0}, {1} and {2}'.format(l[l_index][i][0], l[l_index][j][0], l[l_index][k][0]))
    log.write('\n \n')
    log.close()
    print 'Chose reflections {0}, {1} and {2}, now making mock data...'.format(l[l_index][i][0], l[l_index][j][0], l[l_index][k][0])
    mock_data = [add_rot_error(dat) for dat in mock_data]
    rand_rot = random_rotation()
    mock_data = rm.rotate_list(rand_rot, mock_data)
    all_vectors_rot = rm.rotate_list(rand_rot, all_vectors)
#     ax = fig.add_subplot(312, projection='3d')
#     f.plot_vectors(all_vectors_rot, fig, ax)
    print 'Created mock data. Now running tests...'
    if test_data(mock_data, all_vectors_rot, all_vectors, mycrys,i, j, k, old_filter, vectors):
        return True
    else:
        return False

cif_list = ['Cubic.cif', 'Hexagonal.cif', 'icsd_29288-Si.cif',
            'Monoclinic.cif', 'NiCO3_icsd_61067.cif', 'Orthorhombic.cif',
            'Tetragonal.cif', 'Triclinic.cif', 'Trigonal_hexlatt.cif',
            'Trigonal_rhombolatt_hexaxes.cif',
            'Trigonal_rhombolatt_rhomboaxes.cif']#, 'YMn2O5_icsd_165870.cif']
passed = 0
failled = 0
new_passed = 0
new_failled = 0
filter_failled = 0
i = 0
new_i = 0
start_time = time.time()
max_time = 7200
while True:
    test = 'Start over'
    while test == 'Start over':
        test = test_at_random(cif_list, True)
#         plt.show()
    if test is True:
        passed+=1
    elif test is False:
        failled+=1
    i+=1
    current_time = time.time()
    time_so_far = current_time - start_time
    log = open('test_log_with_error.txt', 'a')
    log.write('For old filter:')
    log.write(str(i) + ' tried ' + str(passed) + ' passed ' + str(failled) +' failled time so far: ' + str(time_so_far))
    log.write('\n \n')
    log.close()
    print 'For old filter: '
    print i,'tried', passed, 'passed', failled,'failled', 'time so far:', time_so_far
    print
    print
    test = 'Start over'
    while test == 'Start over':
        test = test_at_random(cif_list, False)
#         plt.show()
    if test is True:
        new_passed+=1
    elif test is False:
        new_failled+=1
    elif type(test) == list:
        filter_failled+=1
        cif_list = test
    new_i+=1
    current_time = time.time()
    time_so_far = current_time - start_time
    log = open('test_log_with_error.txt', 'a')
    log.write('For new filter: ')
    log.write(str(new_i) + ' tried ' + str(new_passed) + ' passed ' + str(new_failled) +' failled ' + str(filter_failled) + ' failled due to filter time so far: ' + str(time_so_far))
    log.write('\n \n')
    log.close()
    print 'For new filter: '
    print new_i,'tried', new_passed, 'passed', new_failled,'failled', filter_failled, 'failled due to filter', 'time so far:', time_so_far
    print
    print 
    if time_so_far > max_time:
        break

print passed, failled
# plt.show