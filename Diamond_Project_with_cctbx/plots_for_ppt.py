import scisoftpy as dnp
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
import finding_the_rotation_matrix as rm
import copy
import scitbx.math as scm
from scitbx.matrix import col as Vector
from scitbx.matrix import sqr as Rotator
from matplotlib.patches import Arc

#  three_vectors.png
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
all_vectors =[]
for group in l:
    all_vectors+=f.momentum_transfer_vectors(group, mycrys)
l_index = 0
vectors = f.momentum_transfer_vectors(l[l_index], mycrys)
M = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(vectors[0].cross(vectors[2]).cross(Vector((0,0,-10))), dnp.arccos((vectors[0]+vectors[2]).normalize().dot(Vector((0,0,1)))))) 
vectors = rm.rotate_list(M, vectors)
M2 = Rotator(scm.r3_rotation_axis_and_angle_as_matrix((vectors[0]+vectors[2]), dnp.pi)) 
vector = M2*vectors[4]
vectors = rm.rotate_list(M.transpose(), vectors)
fig = plt.figure()
ax = fig.add_subplot(211, projection='3d')
f.plot_vectors_as_arrows([vectors[0]], fig, ax, color='red')
f.plot_vectors_as_arrows([vectors[2]], fig, ax, color='blue')
f.plot_vectors_as_arrows([vectors[4]], fig, ax, color='orange')
f.plot_sphere(vectors[0].length(),fig,ax,True)

ax = fig.add_subplot(212, projection='3d')
f.plot_vectors_as_arrows(all_vectors, fig, ax)

plt.show()