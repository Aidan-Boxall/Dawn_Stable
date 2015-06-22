import numpy as np

import quaternion


def unit_vector(vector):
    """Returns a unit vector in the same direction as vector"""
    return vector / np.linalg.norm(vector)


def convert_to_radians(angle):
    """Converts an angle in degrees to radians"""
    return angle * (np.pi/180.0)


def rotation_to_quaternion(vector, angle):
    """Converts a rotation in terms of an angle and unit vector into a
    quaternion.

    Args:
        axis: The vector in the direction of the axis of rotation.

        angle The angle through which the rotation is made. It has to
            be passed in degrees.

    Returns:
        A quaternion that performs the rotation.
    """
    axis = unit_vector(vector)
    angle = convert_to_radians(angle)

    _ = axis * np.sin(angle/2)

    q = np.quaternion(np.cos(angle/2), _[0], _[1], _[2])

    return q


def rotate(vector, quaternion):
    """Rotates a vector using a quaternion.

    Args:
        vector: The vector which is to be rotated.

        quaternion: The quaternion which describes the rotation.

    Returns:
        The rotated vector.
    """
    vector = np.quaternion(0, vector[0], vector[1], vector[2])
    new_vector = quaternion * vector * np.conjugate(quaternion)
    new_vector = np.array(new_vector.imag)
    return new_vector

def change_in_momentum(momentum_in, axis_of_rotation, two_theta):
    """Finds the change in momentum vector given momentum in, the axis of
    functions and the two theta angle

    Args:
        momentum_in: The momentum vector of the incident beam. Units keV/c.

        axis_of_rotion: The axis perpendicular to the difraction plane centred
            on the sample.

        two_theta: The two_theta angle of difraction. Angle must be passed in
            degrees.

    Returns:
        change_in_momentum: The change in momentum vector.
    """
    _quaternion = rotation_to_quaternion(axis_of_rotation, two_theta)
    momentum_out = rotate(momentum_in, _quaternion)
    return momentum_out - momentum_in
