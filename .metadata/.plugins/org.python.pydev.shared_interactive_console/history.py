shi.sahpe
chi.sahpe
chi.shape
chi[:,0]
chi[:,:-1]
chi[:,[:-1]]
chi[:,range(len(chi[:,0]))-1]
len(chi[:,0]))-1
len(chi[:,0])-1
chi[:,range(len(chi[:,0])-1]
            
)
range(len(chi[:,0])-1
      )
range(len(chi[:,0])-1)
chi[:,range(len(chi[:,0])-1]
)
chi[:,range(len(chi[:,0])-1)]
chi[range(len(chi[:,0])-1),0]
chi[range(1,len(chi[:,0])-1),0]
dnp.plot.surface(roi_sums,chi[range(1,len(chi[:,0])-1),0],kphi[0])
dnp.plot.image(roi_sums,chi[range(1,len(chi[:,0])-1),0],kphi[0])
dnp.plot.image(roi_sums)
dnp.plot.image(roi_sums, name= 'hi')
dnp.plot.image(roi_sums, name= 'hip')
dnp.plot.image(roi_sums, name= 'hi')
dnp.plot.surface(roi_sums,chi[range(1,len(chi[:,0])-1),0],kphi[0], name = 'surface')
dnp.plot.surface(roi_sums,chi[range(1,kphi[0],len(chi[:,0])-1),0], name = 'surface')
dnp.plot.surface(roi_sums, chi[range(1,len(chi[:,0])-1),0], kphi[0], name = 'surface')
dnp.plot.surface(roi_sums, chi[range(1,len(chi[:,0])-1),0], range(10), name = 'surface')
dnp.plot.surface(roi_sums, chi[range(1,len(chi[:,0])-1),0], range(10), name = 'surface')
dnp.plot.surface(roi_sums, chi[:,0], range(10), name = 'surface')
dnp.plot.surface(roi_sums)
dnp.plot.surface(roi_sums, chi[:,0], range(10), name = 'surface')
dnp.plot.surface(roi_sums, name = 'surface')
dnp.plot.image(roi_sums,chi[range(1,len(chi[:,0])-1),0],kphi[0], name=surface)
dnp.plot.image(roi_sums,chi[range(1,len(chi[:,0])-1),0],kphi[0], name='surface')
dnp.plot.image(roi_sums,chi[:,0],kphi[0], name='surface')
dnp.plot.image(roi_sums,range(8),kphi[0], name='surface')
dnp.plot.image(roi_sums,dnp.array(range(8)),kphi[0], name='surface')
dnp.plot.image(roi_sums,dnp.array(range(20)),kphi[0], name='surface')
dnp.plot.image(roi_sums,dnp.array(range(20)),kphi[0], name='surface')import scisoftpy as dnp
import finding_the_rotation_matrix as rm
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
print l[0]
vectors = f.momentum_transfer_vectors(l[0], mycrys)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
f.plot_vectors(vectors, fig, ax)
f.plot_sphere(vectors[0].modulus(), fig, ax)
plt.show()
#Configuring Environment, please wait
import scisoftpy as dnp;import sys;sys.executable=''
import scisoftpy as dnp
import finding_the_rotation_matrix as rm
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
print l[0]
vectors = f.momentum_transfer_vectors(l[0], mycrys)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
f.plot_vectors(vectors, fig, ax)
f.plot_sphere(vectors[0].modulus(), fig, ax)
plt.show()
cd
cd /home/ljh75651/DAWN_stable
cd /home/ljh75651/DAWN_stable/Diamond_Project
import scisoftpy as dnp
import finding_the_rotation_matrix as rm
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
print l[0]
vectors = f.momentum_transfer_vectors(l[0], mycrys)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
f.plot_vectors(vectors, fig, ax)
f.plot_sphere(vectors[0].modulus(), fig, ax)
plt.show()
mock_data = vectors[1:]
print mock_data
print mock_data
mock_data = vectors[:2]
print mock_data
f.plot_vectors(mock_data, fig, ax)
f.plot_sphere(mock_data[0].modulus(), fig, ax)
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
mock_data = vectors[:2]
f.plot_vectors(mock_data, fig, ax)
f.plot_sphere(mock_data[0].modulus(), fig, ax)
plt.show()
mock_data = [vectors[0],vectors[2]]
f.plot_vectors(mock_data, fig, ax)
f.plot_sphere(mock_data[0].modulus(), fig, ax)
plt.show()
mock_data = [vectors[0],vectors[2]]
f.plot_vectors(mock_data, fig, ax)
f.plot_sphere(mock_data[0].modulus(), fig, ax)
plt.show()
mock_data
mock_data[0]
mock_data[0].modulus()
mock_data[0].modulus
mock_data[0].modulus
mock_data[0].modulus()
import scisoftpy as dnp
import finding_the_rotation_matrix as rm
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
print l[0]
vectors = f.momentum_transfer_vectors(l[0], mycrys)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
mock_data = [vectors[0],vectors[2]]
f.plot_vectors(mock_data, fig, ax)
f.plot_sphere(mock_data[0].modulus(), fig, ax)
plt.show()
import scisoftpy as dnp
import finding_the_rotation_matrix as rm
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
print l[0]
vectors = f.momentum_transfer_vectors(l[0], mycrys)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
mock_data = [vectors[0],vectors[2]]
f.plot_vectors(mock_data, fig, ax)
f.plot_sphere(mock_data[0].modulus(), fig, ax)
plt.show()
help(dnp.random)
dnp.random.rand()
dnp.rand()
dnp.random.rand()
dnp.random.rand()
dnp.random.rand()
dnp.random.randint(0,361)
import scisoftpy as dnp
import finding_the_rotation_matrix as rm
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
def random_rotation(vector):
    random_rotation = rm.Rotator(rm.Vector(dnp.random.rand(),dnp.random.rand(),dnp.random.rand()),dnp.random.randint(0,361))
    return random_rotation*vector
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
print l[0]
vectors = f.momentum_transfer_vectors(l[0], mycrys)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
mock_data = [vectors[0],vectors[2]]
target_data = [vectors[0],vectors[2]]
mock_data[0] = random_rotation(mock_data[0])
f.plot_vectors(mock_data, fig, ax)
f.plot_sphere(mock_data[0].modulus(), fig, ax)
plt.show()
print mock_data[0]
print target_data[0]
import scisoftpy as dnp
import finding_the_rotation_matrix as rm
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
def random_rotation(vector_list):
    random_rotation = rm.Rotator(rm.Vector(dnp.random.rand(),dnp.random.rand(),dnp.random.rand()),dnp.random.randint(0,361))
    for vector in vector_list:
        vector = random_rotation * vector
    return vector_list
mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
l = f.group_reflections(mycrys)
print l[0]
vectors = f.momentum_transfer_vectors(l[0], mycrys)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
mock_data = [vectors[0],vectors[2]]
target_data = [vectors[0],vectors[2]]
