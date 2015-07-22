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


def add_rot_error(vector):
    stddev = 0.1
#             rand_rotation_x = rm.Rotator(rm.Vector(1),stddev)#,dnp.random.normal(0,stddev))
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

mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
vectors =[]
#         l_index = 16#3
#         vectors = f.momentum_transfer_vectors(l[l_index], mycrys)
while len(vectors)<3 or len(vectors)>7:
    l_index = dnp.random.randint(len(l))
    vectors = f.momentum_transfer_vectors(l[l_index], mycrys)
    if len(vectors)>4:
        M = scm.matrix.sqr(vectors[0].elems + vectors[2].elems + vectors[4].elems)
        if dnp.abs(M.determinant())<10**-3 and len(vectors)>4:
            vectors = [0,1,2,3,4,5,6,7,8]#len9>8
# f.plot_vectors(vectors)
#         plt.show()
all_vectors=[]
for i, group in enumerate(l):
    all_g = f.momentum_transfer_vectors(group, mycrys)
    all_vectors += all_g
f.plot_vectors(all_vectors)
# fig = plt.figure()
# ax = fig.add_subplot(311, projection='3d')
# f.plot_vectors(all_vectors, fig, ax)
# all_vectors_copy = copy.deepcopy(all_vectors)
# dot = 0
# while dot<10**(-5) or 179.9<dot<180.1:
#     i = dnp.random.randint(len(vectors))
#     j=i
#     k=i
#     while i == j:
#             j = dnp.random.randint(len(vectors))
#     while i==k or j==k:
#         k = dnp.random.randint(len(vectors))
#         if k!=j and k!=i:
#             if dnp.abs(180-dnp.rad2deg(dnp.arccos(vectors[k].normalize().dot(vectors[i].normalize()))))%180.0 < 1:
#                 k=i
#             if dnp.abs(180-dnp.rad2deg(dnp.arccos(vectors[k].normalize().dot(vectors[j].normalize()))))%180.0 < 1:
#                 k=j
#     dot = dnp.rad2deg(dnp.arccos(vectors[i].normalize().dot(vectors[j].normalize())))
# print l_index, i, j, k
# i =0
# j=4
# k=3
# mock_data = [vectors[i], vectors[j], vectors[k]]
# mock_data = [add_rot_error(dat) for dat in mock_data]
# figm = plt.figure(3)
# axm = figm.add_subplot(211, projection='3d')
# f.plot_vectors([mock_data[0]], figm, axm, color='green')
# f.plot_vectors([mock_data[1]], figm, axm, color='blue')
# f.plot_vectors([mock_data[2]], figm, axm, color='red')
# f.plot_sphere(mock_data[0].length(), figm, axm)
# rand_rot = random_rotation()
# mock_data = rm.rotate_list(rand_rot, mock_data)
# all_vectors_copy = rm.rotate_list(rand_rot, all_vectors_copy)
# ax = fig.add_subplot(312, projection='3d')
# f.plot_vectors(all_vectors_copy, fig, ax)
# U = u.find_U_matrix(mock_data, mycrys)
# rotator = U
# all_vectors_copy = rm.rotate_list(rotator, all_vectors_copy)
# ax = fig.add_subplot(313, projection='3d')
# f.plot_vectors(all_vectors_copy, fig, ax)
#         print 'Orientation', rand_rot
#         print 'U matrix', rotator



import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d.art3d import juggle_axes




temp_data = []
axis = Vector([0, 0, 1.0])
angle =10
R = Rotator(scm.r3_rotation_axis_and_angle_as_matrix(axis, angle, deg=True))
for i in range(360):
    temp_data.append(all_vectors)
    all_vectors = rm.rotate_list(R, all_vectors)

temp_data2 = []

for tdat in temp_data:
    tdat2=[]
    for v in range(len(tdat)):
        tdat2.append(tdat[v].elems)
        if v ==10:
            break
    temp_data2.append(tdat2)

data = []
for tdat2 in temp_data2:
    data.append(zip(*tdat2))
print len(data)

def run(num, data, points):
    # update the data
    print num
    print len(data[num][0])
    points._offsets3d = juggle_axes(data[num][0],data[num][1],data[num][2], 'z')
    return range(num-1)

fig = plt.figure()
ax = p3.Axes3D(fig)
# fig, ax = plt.subplots()
points = ax.scatter(data[0][0],data[0][1],data[0][2], depthshade=True, s=30, animated=True)

# ax.set_ylim(-1.1, 1.1)
# ax.set_xlim(0, 5)
# ax.grid()
# xdata, ydata = [], []
 

ax.set_xlim3d([-2.0, 2.0])
ax.set_xlabel('X')

ax.set_ylim3d([-2.0, 2.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-2.0, 2.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

ani = animation.FuncAnimation(fig, run, 25, fargs=(data, points), blit=True, interval=1000,
    repeat=False)
plt.show()


