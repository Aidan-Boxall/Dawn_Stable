import scisoftpy as dnp
import finding_the_rotation_matrix as rm
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
import copy

def add_rot_error(vector):
    stddev = 0.1
    rand_rotation_x = rm.Rotator(rm.Vector(1),dnp.random.normal(0,stddev))
    rand_rotation_y = rm.Rotator(rm.Vector(0,1), dnp.random.normal(0,stddev))
    rand_rotation_z = rm.Rotator(rm.Vector(0,0,1),dnp.random.normal(0,stddev))
    vector = rand_rotation_z * rand_rotation_y * rand_rotation_x * vector
    return vector

def random_rotation(vector_list):
    rand_rotation_x = rm.Rotator(rm.Vector(1),dnp.random.randint(0,361))
    rand_rotation_y = rm.Rotator(rm.Vector(0,1),dnp.random.randint(0,361))
    rand_rotation_z = rm.Rotator(rm.Vector(0,0,1),dnp.random.randint(0,361))
    for i, vector in enumerate(vector_list):
        vector = rand_rotation_z * rand_rotation_y * rand_rotation_x * vector
        vector_list[i] = vector
    return vector_list

def rotations(vector_list,n=1):
    while n>0:
        vector_list = random_rotation(vector_list)
        n-=1
    return vector_list

def rotate_list(rotation, vector_list):
    for i, vector in enumerate(vector_list):
        vector = rotation * vector
        vector_list[i] = vector
    return vector_list

m = 1
t = 1

mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
vectors = f.momentum_transfer_vectors(l[0], mycrys)
target_data = [vectors[1], vectors[5]]
# mock_data = [add_rot_error(target) for target in target_data]
mock_data = [vectors[1], vectors[5]]#+[vectors[0]]+vectors[3:]

fig = plt.figure(1)
ax = fig.add_subplot(231)
f.stereographic_projection(vectors, fig,ax, color = 'blue')

ax = fig.add_subplot(232)
f.stereographic_projection(mock_data, fig,ax, color = 'blue')
# f.stereographic_projection(target_data, fig,ax)
mock_data = rotations(mock_data, 10)


ax = fig.add_subplot(234)
f.stereographic_projection(mock_data, fig,ax, color = 'blue')
# f.stereographic_projection(target_data, fig,ax)


r = rm.get_rotator(mock_data[0], target_data[0])
mock_data = rotate_list(r, mock_data)

ax = fig.add_subplot(235)
f.stereographic_projection(mock_data, fig,ax, color = 'blue')
# f.stereographic_projection(target_data, fig,ax)
# f.plot_sphere(mock_data[0].modulus(), fig, ax)

r2 = rm.get_second_rotator(target_data[0], mock_data[m], target_data[t])
mock_data = rotate_list(r2, mock_data)

ax = fig.add_subplot(236)
f.stereographic_projection(mock_data, fig,ax, color = 'blue')
# f.stereographic_projection(target_data, fig,ax)

r3 = r*r2
print r3.R

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# # r3 = rm.get_third_rotator(target_data[0], mock[1], target_data[1])
# mock = rotate_list(r, mock)
# mock = rotate_list(r2, mock)
# f.plot_vectors(mock, fig, ax, color = 'red')
# f.plot_vectors(target_data, fig, ax)
# f.plot_sphere(mock_data[0].modulus(), fig, ax)



plt.show()