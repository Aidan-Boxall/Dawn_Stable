non_equiv_unit = [vector.unit() for vector in non_equiv]
vectors += non_equiv
ax = fig.add_subplot(231)
f.stereographic_projection(vectors_unit, fig,ax, color = 'blue')
#f.stereographic_projection(non_equiv_unit, fig,ax, color = 'green')
ax2 = fig2.add_subplot(231, projection='3d')
f.plot_vectors(vectors[:6], fig2, ax2)
f.plot_sphere(mock_data[0].modulus(), fig2, ax2)
ax = fig.add_subplot(232)
f.stereographic_projection(target_data, fig,ax, color = 'blue')
ax2 = fig2.add_subplot(232, projection='3d')
f.plot_vectors(target_data, fig2, ax2)
f.plot_sphere(mock_data[0].modulus(), fig2, ax2)
# f.stereographic_projection(target_data, fig,ax)
# Apply first rotation
r = rm.get_rotator(mock_data[0], target_data[0])
mock_data = rm.rotate_list(r, mock_data)
# Plot after first rotation
ax = fig.add_subplot(235)
unit_mock_data = [dat.unit() for dat in mock_data]
ax2 = fig2.add_subplot(235, projection='3d')
f.plot_vectors(mock_data[:9], fig2, ax2)
f.plot_sphere(mock_data[0].modulus(), fig2, ax2)
xs= []
ys=[]
t = f.stereographic_projection([unit_mock_data[0]], fig,ax, color = 'black')
xs.append(t[0][0])
ys.append(t[1][0])
t = f.stereographic_projection([unit_mock_data[1]], fig,ax, color = 'green')
xs.append(t[0][0])
ys.append(t[1][0])
t = f.stereographic_projection([unit_mock_data[2]], fig,ax, color = 'orange')
xs.append(t[0][0])
ys.append(t[1][0])
t = f.stereographic_projection([unit_mock_data[3]], fig,ax, color = 'blue')
xs.append(t[0][0])
ys.append(t[1][0])
axis_params = [dnp.absolute(min(xs))*1.1, max(xs)*1.1,dnp.absolute(min(ys))*1.1,max(ys)*1.1]
fig_len=max(axis_params)*1.1
ax.axis([-fig_len,fig_len,-fig_len,fig_len])
# Apply second rotation
r2 = rm.get_second_rotator(target_data[0], mock_data[1], target_data[1])
mock_data = rm.rotate_list(r2, mock_data)
# Plot after second rotation
ax = fig.add_subplot(236)
unit_mock_data = [dat.unit() for dat in mock_data]
ax2 = fig2.add_subplot(236, projection='3d')
f.plot_vectors(mock_data[:9], fig2, ax2)
f.plot_sphere(mock_data[0].modulus(), fig2, ax2)
xs= []
ys=[]
t = f.stereographic_projection([unit_mock_data[0]], fig,ax, color = 'black')
xs.append(t[0][0])
ys.append(t[1][0])
t = f.stereographic_projection([unit_mock_data[1]], fig,ax, color = 'green')
xs.append(t[0][0])
ys.append(t[1][0])
t = f.stereographic_projection([unit_mock_data[2]], fig,ax, color = 'orange')
xs.append(t[0][0])
ys.append(t[1][0])
t = f.stereographic_projection([unit_mock_data[3]], fig,ax, color = 'blue')
xs.append(t[0][0])
ys.append(t[1][0])
axis_params = [dnp.absolute(min(xs))*1.1, max(xs)*1.1,dnp.absolute(min(ys))*1.1,max(ys)*1.1]
fig_len=max(axis_params)*1.1
ax.axis([-fig_len,fig_len,-fig_len,fig_len])
# Define U matrix rotator
U = r2 * r
# Optimising the U matrix
def diff(array, data, vectors):
    x = array[0]
    y = array[1]
    z = array[2]
    angle = array[3]
    axis = rm.Vector(x,y,z)
    U = rm.Rotator(axis, angle)
    data = rm.rotate_list(U, data)
    index_list=[]
    for i, dat in enumerate(data):
        diffs = []
        for j, vector in enumerate(vectors):
            diffs.append((dat-vector).modulus())
        index = diffs.index(min(dnp.abs(diffs)))
        index_list.append(index)
    targets = [0]*len(data)
    for i, idx in enumerate(index_list):
        targets[i] = vectors[idx]
    total = 0
    for i, dat in enumerate(data):
        total += (dat - targets[i]).modulus()
    return total
axis = U.axis
array = dnp.array([axis.x, axis.y, axis.z, U.angle])
print diff(array, data, vectors)
data_unit = [dat.unit() for dat in data]
import scipy.optimize
opt = scipy.optimize.minimize(diff, array, (data_unit, vectors_unit))
print opt
print array
print opt.x
print diff(opt.x,data,vectors)
axis = rm.Vector(opt.x[0], opt.x[1], opt.x[2])
new_U = rm.Rotator(axis, opt.x[3])
data_unit2 = [dat.unit() for dat in data2]
new = rm.rotate_list(new_U, data_unit2)
fig = plt.figure(3)
ax = fig.add_subplot(121)
f.stereographic_projection(new[:3], fig,ax, color = 'blue')
ax2 = fig.add_subplot(122, projection='3d')
f.plot_vectors(new[:9], fig, ax2)
f.plot_sphere(new[0].modulus(), fig, ax2)
print U
print new_U
plt.show()
x = Vector(0.866025403784, -5.55111512313e-17, 0.0)
x = rm.combinations(iterable, r)Vector(0.866025403784, -5.55111512313e-17, 0.0)
x = rm.Vector(0.866025403784, -5.55111512313e-17, 0.0)
y = rm.Vector(-0.866025403784, 1.11022302463e-16, 0.0)
print x**y
#Configuring Environment, please wait
import scisoftpy as dnp;import sys;sys.executable=''
round(-5)
#Configuring Environment, please wait
import scisoftpy as dnp;import sys;sys.executable=''
#Configuring Environment, please wait
import scisoftpy as dnp;import sys;sys.executable=''
import scitbx.math as scm
from scitbx.matrix import col as Vector
x = Vector([1,2,3])
x
x.elems
#Configuring Environment, please wait
import scisoftpy as dnp;import sys;sys.executable=''
import scisoftpy as dnp
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
import finding_the_rotation_matrix as rm
import finding_the_U_matrix as u
import copy
import scitbx.math as scm
from scitbx.matrix import col as Vector
from scitbx.matrix import sqr as Rotator
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
cd
cd '~/DAWN_stable/Diamond_Project_with_cctbx'
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
all_vectors=[]
for i, group in enumerate(l):
    all_g = f.momentum_transfer_vectors(group, mycrys)
    all_vectors += all_g
zip(all_vectors)
for vector in all_vectors:
    vector = vector.elems
    
for vector in all_vectors:
    vector = vector.elems
    
for vector in all_vectors:
    vector = vector.dnp_array()
    
import scisoftpy as dnp
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
import finding_the_rotation_matrix as rm
import finding_the_U_matrix as u
import copy
import scitbx.math as scm
from scitbx.matrix import col as Vector
from scitbx.matrix import sqr as Rotator
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
all_vectors=[]
for i, group in enumerate(l):
    all_g = f.momentum_transfer_vectors(group, mycrys)
    all_vectors += all_g
for vector in all_vectors:
    vector = vector.elems
    
for vector in all_vectors:
    vector = vector
Vector
cd
cd '~/DAWN_stable/Diamond_Project_with_cctbx'
cd
pwd '~/DAWN_stable/Diamond_Project_with_cctbx'
pwd '~/DAWN_stable/Diamond_Project_with_cctbx'
wd '~/DAWN_stable/Diamond_Project_with_cctbx'
wd ~/DAWN_stable/Diamond_Project_with_cctbx
cwd ~/DAWN_stable/Diamond_Project_with_cctbx
cwd '~/DAWN_stable/Diamond_Project_with_cctbx'
cd '~/DAWN_stable/Diamond_Project_with_cctbx'
pwd
reload(f)
