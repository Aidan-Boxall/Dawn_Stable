import unittest


class TestUnit(unittest.TestCase):

    def test_rotation(self):
        import numpy as np
        import functions as f
        axis = np.array([0, 0, 1])
        x = np.array([1, 0, 0])
        angle = 45
        quaternion = f.rotation_to_quaternion(axis, angle)
        print f.rotate(x, quaternion)
 
 
    def test_change_in_momentum(self):
        import numpy as np
 
        import functions as f
        # Tests the change in momentum code.
        # Uses the beamline as the x-axis and the vertical as the z axis.
        # For testing purposes assumes the axis of functions is the y axis and
        #     the diffracted beam is the x-z plane.
 
        Y_AXIS = np.array([0, -1.0, 0])  # The negative y axis is the axis of
        #                                     functions for the momentum.
        energy = 8
        momentum_in = np.array([energy, 0, 0])
        two_theta = 45
        print f.unit_vector(
            f.change_in_momentum(momentum_in, Y_AXIS, two_theta))
 
 
    def test_reflection_plotting(self):
        import functions as f
        import Crystal as c
        import numpy as np
        import matplotlib.pyplot as plt
 
 
        from mpl_toolkits.mplot3d import Axes3D
        mycrys = c.Crystal()
        mycrys.load_cif('icsd_29288-Si.cif')
 
        grouped_reflections = f.group_reflections(mycrys,8)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
 
        for i, group in enumerate(grouped_reflections):
            print i, len(group)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            vectors = f.momentum_transfer_vectors(grouped_reflections[i],
                                                   mycrys)
            f.plot_vectors(vectors,fig,ax)
            f.plot_sphere(np.linalg.norm(vectors[0]),fig,ax)
        plt.show()
 
    def test_stereogaphic_projection(self):
        import functions as f
        import Crystal as c
        import numpy as np
        import matplotlib.pyplot as plt


        mycrys = c.Crystal()
        mycrys.load_cif('icsd_29288-Si.cif')

        grouped_reflections = f.group_reflections(mycrys,8)
        for i, group in enumerate(grouped_reflections):
            vectors = f.momentum_transfer_vectors(grouped_reflections[i],
                                                  mycrys)
            print i, len(group)
            if i==9:
                f.stereographic_projection(vectors)
        plt.show()

if __name__ == '__main__':
    unittest.main()
