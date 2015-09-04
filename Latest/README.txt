Steps to orientate the crystal:

1. Find the Bragg reflections to be measured using reflection_choice function from reflection_choice.py If you want to change the factor weightings they can be found in the choose_reflection function from this file. Then reflection_choice function returns a Jython script for the detector as string.
2. Fix the parameters in pixel_vector_find_qs.py, pixel_vectors_find_rotations.py and pixel_to_vector_fix_nexus.py.
3. Run script.sh this gets around the dials issue.
4. Run script  pixel_vectors_find_rotations.py and save the outputted vectors eg in a pickle file.
5. Pass the vectors through find_U_matrix function in finding_the_rotation_matrix.py, this returns the U matrix.
