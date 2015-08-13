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
import pickle

def arccos(x):
    if x < -1:
        return dnp.arccos(-1)
    if x >  1:
        return dnp.arccos(1)
    else:
        return dnp.arccos(x)

def draw_vectors():
    files =[]
    cif = 'NiCO3_icsd_61067.cif'
    mycrys = c.Crystal()
    mycrys.load_cif(cif)
    f.momentum_transfer_vectors(group, crystal)
    refl = 'allowed'
    grouped_reflections = f.group_reflections(mycrys, energy=8, refl=refl)
    vectors = f.get
    axis_chi = Vector((0,1,0))
    angle_chi = 90.0
    angle_chis = 90.0/200
    chi_step = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(axis_chi, angle_chis, deg = True))
    axis_p = Vector((0,0,1))
    angle_p = 360
    angle_ps = angle_p/20.0
    phi_step = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(axis_p, angle_ps, deg = True))
    prefix='cubrot_'
    i=-1
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-4,4)
    ax.set_ylim(-4,4)
    ax.set_zlim(-4,4)
    f.plot_vectors_wireframe(cuboid_vectors, fig, ax)
    fname = '%s%03d.jpeg'%(prefix,i)
    ax.figure.savefig(fname)
    files.append(fname)
    for j in range(21):
#         if j!=0:

#             axis_p = rm.rotate_list(chi_step, [axis_p])[0]
#             phi_step = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(axis_p, angle_ps, deg = True))
            for i in range(30*j, 30*j+10):
                cuboid_vectors = rm.rotate_list(chi_step, cuboid_vectors)
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.set_xlim(-4,4)
                ax.set_ylim(-4,4)
                ax.set_zlim(-4,4)
                f.plot_vectors_wireframe(cuboid_vectors, fig, ax)
                fname = '%s%03d.jpeg'%(prefix,i)
                print i
                ax.figure.savefig(fname)
                files.append(fname)
            for i in range(30*j+10,(30*j)+30):
                cuboid_vectors = rm.rotate_list(phi_step, cuboid_vectors)
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.set_xlim(-4,4)
                ax.set_ylim(-4,4)
                ax.set_zlim(-4,4)
                f.plot_vectors_wireframe(cuboid_vectors, fig, ax)
                fname = '%s%03d.jpeg'%(prefix,i)
                print i
                ax.figure.savefig(fname)
                files.append(fname)
    return files

if __name__ == '__main__':
    files = draw_cuboid()
    an.rotanimate(files, "cuboid_rot.mp4")
    with open('cube_files.pkl', 'wb')  as file:
        pickle.dump(files, file)
#     if not test_by_hkl(cif, hkl_list, add_error=False, old_filter=False, create_plots=False):
#         break
