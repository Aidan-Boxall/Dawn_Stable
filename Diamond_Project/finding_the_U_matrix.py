import scisoftpy as dnp
import finding_the_rotation_matrix as rm
import Crystal as c
import functions as f
import matplotlib.pyplot as plt
import copy


def find_U_matrix(found_vectors, crystal, beam_energy=8, optimise_U=True):
    """Given a Crystal class object with a cif file loaded into it, this
    function returns the U matrix as a dnp array.

    Args:
        found_vectors: A list of Vector class objects representing the momentum
            transfer vectors of the measured Bragg peaks.

        crystal: A Crystal class object.

        beam_energy: The beam energy in keV.

        optimise_U: If True the function optimises the U matrix before returning
            can be set to False if in Jython because requires scipy.

    Returns:
        U: The U matrix as a dnp object.
    """
    # First gets all the allowed momentum transfer vectors of the crystal.
    grouped_reflections = f.group_reflections(crystal, beam_energy)
    all_vectors = []
    for i, group in enumerate(grouped_reflections):
        group_vectors = f.momentum_transfer_vectors(group, crystal)
        all_vectors += group_vectors
    # Find the target vectors.
    target_vectors = rm.finding_the_targets(found_vectors, all_vectors)
    found_vectors_copy = copy.deepcopy(found_vectors)
    # Find and apply the first rotation.
    r1 = rm.get_rotator(found_vectors[0], target_vectors[0])
    found_vectors = rm.rotate_list(r1, found_vectors)

    # Find the second rotation
    r2 = rm.get_second_rotator(target_vectors[0], found_vectors[1], 
                                    target_vectors[1])

    U = r2 * r1

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
            dat = dat
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

    if not optimise_U:
        return U.R
    elif optimise_U:

        axis = U.axis
        # The array gives a first estimate for the arguments for the diff
            # function.
        array = dnp.array([axis.x, axis.y, axis.z, U.angle])
        import scipy.optimize
        optimise = scipy.optimize.minimize(diff, array, (found_vectors_copy, 
            all_vectors), bounds=[(-1,1),(-1,1),(-1,1),(0,360)])
        if optimise['success']:
            new_axis = rm.Vector(optimise.x[0], optimise.x[1], optimise.x[2])
            new_U = rm.Rotator(new_axis, optimise.x[3])
            return new_U.R
        else:
            print 'U matrix optimisation failed.'
            return U.R
    else:
        raise Exception("""optimise_U must be a boolean type""")