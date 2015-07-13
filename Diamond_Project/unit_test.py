import unittest


class TestUnit(unittest.TestCase):

#     def test_rotation(self):
#         import numpy as np
#         import functions as f
#         axis = np.array([0, 0, 1])
#         x = np.array([1, 0, 0])
#         angle = 45
#         quaternion = f.rotation_to_quaternion(axis, angle)
#         print f.rotate(x, quaternion)
 
 
#     def test_change_in_momentum(self):
#         import numpy as np
#  
#         import functions as f
#         # Tests the change in momentum code.
#         # Uses the beamline as the x-axis and the vertical as the z axis.
#         # For testing purposes assumes the axis of functions is the y axis and
#         #     the diffracted beam is the x-z plane.
#  
#         Y_AXIS = np.array([0, -1.0, 0])  # The negative y axis is the axis of
#         #                                     functions for the momentum.
#         energy = 8
#         momentum_in = np.array([energy, 0, 0])
#         two_theta = 45
#         print f.unit_vector(
#             f.change_in_momentum(momentum_in, Y_AXIS, two_theta))
 
 
#     def test_reflection_plotting(self):
#         import functions as f
#         import Crystal as c
#         import numpy as np
#         import matplotlib.pyplot as plt
#  
#  
#         from mpl_toolkits.mplot3d import Axes3D
#         mycrys = c.Crystal()
#         mycrys.load_cif('icsd_29288-Si.cif')
#  
#         grouped_reflections = f.group_reflections(mycrys,8)
#         fig = plt.figure()
#         for i, group in enumerate(grouped_reflections):
#             plot_width=np.sqrt(len(grouped_reflections))+1
#             ax = fig.add_subplot(plot_width,plot_width,i+1, projection='3d')
#             vectors = f.momentum_transfer_vectors(grouped_reflections[i],
#                                                    mycrys)
#             f.plot_vectors(vectors,fig,ax)
#             f.plot_sphere(np.linalg.norm(vectors[0]),fig,ax)
# 
#  
#     def test_stereogaphic_projection(self):
#         import functions as f

#         import Crystal as c
#         import numpy as np
#         import matplotlib.pyplot as plt
# 
# 
#         mycrys = c.Crystal()
#         mycrys.load_cif('icsd_29288-Si.cif')
# 
#         grouped_reflections = f.group_reflections(mycrys,8)
#         fig = plt.figure()
#         for i, group in enumerate(grouped_reflections):
#             plot_width=np.sqrt(len(grouped_reflections))+1
#             ax = fig.add_subplot(plot_width,plot_width,i+1)
#             vectors = f.momentum_transfer_vectors(grouped_reflections[i],
#                                                   mycrys)
#             print i, len(group), grouped_reflections[i][0][4]
#             f.stereographic_projection(vectors,fig,ax)
#         plt.show()

#     def test_plotting(self):
#         import functions as f
#         import Crystal as c
#         import matplotlib.pyplot as plt
# 
# 
#         mycrys = c.Crystal()
#         mycrys.load_cif('NiCO3_icsd_61067.cif')
#         mycrys2 = c.Crystal()
#         mycrys2.load_cif('icsd_29288-Si.cif') 
#         f.many_vector_plots(mycrys,8,1)
#         f.many_stereographic_plots(mycrys,8,10)
#         f.many_vector_plots(mycrys2)
#         f.many_stereographic_plots(mycrys2)
#         plt.show()

    def test_finding_the_U_matrix(self):
        import scisoftpy as dnp
        import Crystal as c
        import functions as f
        import matplotlib.pyplot as plt
        import finding_the_rotation_matrix as rm
        import finding_the_U_matrix as u
        import copy

        def add_rot_error(vector):
            stddev = 0.1
#             rand_rotation_x = rm.Rotator(rm.Vector(1),stddev)#,dnp.random.normal(0,stddev))
#             rand_rotation_y = rm.Rotator(rm.Vector(0,1),-stddev)#, dnp.random.normal(0,stddev))
#             rand_rotation_z = rm.Rotator(rm.Vector(0,0,1),stddev)#,dnp.random.normal(0,stddev))
            rand_axis = rm.Vector(dnp.random.random(),dnp.random.random(),dnp.random.random())
            rand_rotation = rm.Rotator(rand_axis, stddev)
            vector = rand_rotation * vector
            return vector

        def random_rotation():
            rand_rotation_x = rm.Rotator(rm.Vector(1) ,dnp.random.randint(0,361))
            rand_rotation_y = rm.Rotator(rm.Vector(0,1),dnp.random.randint(0,361))
            rand_rotation_z = rm.Rotator(rm.Vector(0,0,1),dnp.random.randint(0,361))
            return rand_rotation_z*rand_rotation_y*rand_rotation_x

        mycrys = c.Crystal()
        mycrys.load_cif('NiCO3_icsd_61067.cif')
        l = f.group_reflections(mycrys)
        vectors = f.momentum_transfer_vectors(l[2], mycrys)
        non_equiv = f.momentum_transfer_vectors(l[1], mycrys)
        all_vectors=[]
        for i, group in enumerate(l):
            all_g = f.momentum_transfer_vectors(group, mycrys)
            all_vectors += all_g
        fig = plt.figure()
        ax = fig.add_subplot(311, projection='3d')
        f.plot_vectors(all_vectors, fig, ax)
        all_vectors_copy = copy.deepcopy(all_vectors)
        mock1 = vectors[dnp.random.randint(0, len(vectors))]
        mock2 = non_equiv[dnp.random.randint(0, len(non_equiv))]
        mock_data = [mock1, mock2] + all_vectors[-8:]
        mock_data = [add_rot_error(dat) for dat in mock_data]
        rand_rot = random_rotation()
        mock_data = rm.rotate_list(rand_rot, mock_data)
        all_vectors_copy = rm.rotate_list(rand_rot, all_vectors_copy)
        ax = fig.add_subplot(312, projection='3d')
        f.plot_vectors(all_vectors_copy, fig, ax)
        U = u.find_U_matrix(mock_data, mycrys)
        rotator = rm.Rotator(R=U)
        all_vectors_copy = rm.rotate_list(rotator, all_vectors_copy)
        ax = fig.add_subplot(313, projection='3d')
        f.plot_vectors(all_vectors_copy, fig, ax)
        print 'Orientation', rand_rot
        print 'U matrix', rotator
        print 'Unitary rotation?', dnp.linalg.det(rotator.R)
        plt.show()



if __name__ == '__main__':

    unittest.main()
