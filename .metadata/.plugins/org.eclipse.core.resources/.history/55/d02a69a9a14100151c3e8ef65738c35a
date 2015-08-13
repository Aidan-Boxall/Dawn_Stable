import scisoftpy as dnp
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
import finding_the_rotation_matrix_animate as rm
import copy
import scitbx.math as scm
from scitbx.matrix import col as Vector
from scitbx.matrix import sqr as Rotator
from itertools import permutations
import time

import animate as an
import pickle

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
    rand_rotation_x = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(Vector([1.0,0,0]) ,0, deg=True))
    rand_rotation_y = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(Vector([0,1.0,0]),0, deg=True))
    rand_rotation_z = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(Vector([0.0,0.0,1.0]),25, deg=True))
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


def test_data(mock_data, all_vectors_rot, all_vectors, mycrys, old_filter, vectors=False, create_plots=True):
    if not old_filter:
        U = rm.find_U_matrix(mock_data, mycrys)
    else:
        U = rm.find_U_matrix(mock_data, mycrys, refl='allowed')

    difference = diff(U, all_vectors_rot, all_vectors)
    if difference > 5:
        create_plots = True

    print 'diff', difference

    if create_plots:
        fig = plt.figure()
    
        ax = fig.add_subplot(311, projection='3d')
        ax.set_title('Unedited Reciprocal Space')
        f.plot_vectors(all_vectors, fig, ax)
    
        ax = fig.add_subplot(312, projection='3d')
        ax.set_title('Randomly Rotated Reciprocal Space')
        f.plot_vectors(all_vectors_rot, fig, ax)
    
        all_vectors_rot = rm.rotate_list(U, all_vectors_rot)
    
        ax = fig.add_subplot(313, projection='3d')
        ax.set_title('Randomly Rotated Reciprocal Space after U Matrix')
        f.plot_vectors(all_vectors_rot, fig, ax)

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



def get_plots_by_hkl(cif, hkl_list, add_error=True, create_plots=True,  old_filter=False, energy=8):
    files = []
    mycrys = c.Crystal()
    mycrys.load_cif(cif)
    if old_filter:
        refl = 'allowed'
    else:
        refl = 'orient'
    grouped_reflections = f.group_reflections(mycrys, energy=energy, refl=refl)
    all_vectors_hkl = []
    all_vectors = []
    for i, group in enumerate(grouped_reflections):
        group_vectors = f.momentum_transfer_vectors(group, mycrys)
        for j, item in enumerate(group):
            vector_hkl = (group_vectors[j], item[0])
            all_vectors_hkl.append(vector_hkl)
            all_vectors.append(group_vectors[j])
    f.plot_vectors(all_vectors)
    plt.show()
    vectors = []
    for hkl in hkl_list:
        for vector in all_vectors_hkl:
            if hkl == vector[1]:
                vectors.append(vector[0])
                break
    rand_rotation = random_rotation()
    print 'Random rot', rand_rotation
    mock_data = rm.rotate_list(rand_rotation, vectors)
    all_vectors_rot = rm.rotate_list(rand_rotation, all_vectors)
    if add_error:
        mock_data = [add_rot_error(dat) for dat in mock_data]
    if not old_filter:
        targets = rm.animation_targets(mock_data, mycrys)
        print f.find_hkls(mycrys, vectors)
    else:
        targets = rm.animation_targets(mock_data, mycrys, refl='allowed')
        f.find_hkls(mycrys, vectors,  refl='allowed')

    rot1list = rm.get_rotator(mock_data[0], targets[0])
    axis1 = rot1list[1]
    angle = rot1list[2]
    print angle
    angle = angle/20.0
    rot1_step = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(axis1, angle))
    
    mock_data = [dat.normalize() for dat in mock_data]
    targets = [target.normalize() for target in targets]
    prefix='tmprot_'
    #Pause
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    f.plot_vectors(all_vectors_rot, fig, ax)
#     f.plot_vectors_as_arrows([targets[0]], fig, ax, color='red')
#     f.plot_vectors_as_arrows([targets[1]], fig, ax, color='blue')
#     f.plot_vectors_as_arrows([mock_data[0]], fig, ax, color='red')
#     f.plot_vectors_as_arrows([mock_data[1]], fig, ax, color='blue')
#     f.plot_sphere(mock_data[0].length(), fig, ax, True)
    print "Pause..."
    for i in range(20):
        fname = '%s%03d.jpeg'%(prefix,i)
        print i
        ax.figure.savefig(fname)
        files.append(fname)

    #First Rotation
    print 'First rotation...'
    for i in range(20, 40):
        print i
        mock_data = rm.rotate_list(rot1_step, mock_data)
        all_vectors_rot = rm.rotate_list(rot1_step, all_vectors_rot)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
#         f.plot_vectors_as_arrows([targets[0]], fig, ax, color='red')
#         f.plot_vectors_as_arrows([targets[1]], fig, ax, color='blue')
#         f.plot_vectors_as_arrows([mock_data[0]], fig, ax, color='red')
#         f.plot_vectors_as_arrows([mock_data[1]], fig, ax, color='blue')
#         f.plot_vectors_as_arrows([axis1], fig, ax, color='black')
#         f.plot_sphere(mock_data[0].length(), fig, ax, True)
        f.plot_vectors(all_vectors_rot, fig, ax)
        fname = '%s%03d.jpeg'%(prefix,i)
        ax.figure.savefig(fname)
        files.append(fname)

    #Pause2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
#     f.plot_vectors_as_arrows([targets[0]], fig, ax, color='red')
#     f.plot_vectors_as_arrows([targets[1]], fig, ax, color='blue')
#     f.plot_vectors_as_arrows([mock_data[0]], fig, ax, color='red')
#     f.plot_vectors_as_arrows([mock_data[1]], fig, ax, color='blue')
#     f.plot_sphere(mock_data[0].length(), fig, ax, True)
    f.plot_vectors(all_vectors_rot, fig, ax)
    print "Pause2..."
    for i in range(40, 60):
        print i
        fname = '%s%03d.jpeg'%(prefix,i)
        ax.figure.savefig(fname)
        files.append(fname)

    #Second_rotation
    rot2list = rm.get_second_rotator(targets[0], mock_data[1], targets[1])
    axis2 = rot2list[1]
    angle = rot2list[2]
    print angle
    angle = angle/20.0
    rot2_step = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(axis2, angle))
    print "Second rotation..."
    for i in range(60, 80):
        print i
        mock_data = rm.rotate_list(rot2_step, mock_data)
        all_vectors_rot = rm.rotate_list(rot2_step, all_vectors_rot)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
#         f.plot_vectors_as_arrows([targets[0]], fig, ax, color='red')
#         f.plot_vectors_as_arrows([targets[1]], fig, ax, color='blue')
#         f.plot_vectors_as_arrows([mock_data[0]], fig, ax, color='red')
#         f.plot_vectors_as_arrows([mock_data[1]], fig, ax, color='blue')
#         f.plot_vectors_as_arrows([axis2], fig, ax, color='black')
#         f.plot_sphere(mock_data[0].length(), fig, ax, True)
        f.plot_vectors(all_vectors_rot, fig, ax)
        fname = '%s%03d.jpeg'%(prefix,i)
        ax.figure.savefig(fname)
        files.append(fname)
    #Pause3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
#     f.plot_vectors_as_arrows([targets[0]], fig, ax, color='red')
#     f.plot_vectors_as_arrows([targets[1]], fig, ax, color='blue')
#     f.plot_vectors_as_arrows([mock_data[0]], fig, ax, color='red')
#     f.plot_vectors_as_arrows([mock_data[1]], fig, ax, color='blue')
#     f.plot_sphere(mock_data[0].length(), fig, ax, True)
    f.plot_vectors(all_vectors_rot, fig, ax)
    print "Pause3..."
    for i in range(80, 81):
        print i
        fname = '%s%03d.jpeg'%(prefix,i)
        ax.figure.savefig(fname)
        files.append(fname)

    return files

if __name__ == '__main__':
    cif = 'NiCO3_icsd_61067.cif'
    hkl_list = [(-2, 0, 16), (2, -2, 16), (0, 2, 16)]
    i = 1
    print i
    while True:
        files = get_plots_by_hkl(cif, hkl_list, add_error=False, old_filter=False, create_plots=True)
        print "Create movie..."
        an.rotanimate(files, "rotation_video2.mp4")
        with open('files.pkl', 'wb')  as file:
            pickle.dump(files, file)
    #     if not test_by_hkl(cif, hkl_list, add_error=False, old_filter=False, create_plots=False):
    #         break
        break

