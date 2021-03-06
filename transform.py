import numpy as np
import math

# Create a indentity matrix
def createEyeMat():
    return np.eye(4)

# Apply translation to the matrix
def translate(tx, ty, mat_transform):
    mat_translation = np.array([[1.0, 0.0, 0.0, tx],
                                [0.0, 1.0, 0.0, ty],
                                [0.0, 0.0, 1.0, 0.0],
                                [0.0, 0.0, 0.0, 1.0]], np.float32)
    return np.dot(mat_translation, mat_transform)

# Apply scale to the matrix
def scale(sx, sy, mat_transform):
    mat_scale = np.array([[sx, 0.0, 0.0, 0.0],
                          [0.0, sy, 0.0, 0.0],
                          [0.0, 0.0, 1.0, 0.0],
                          [0.0, 0.0, 0.0, 1.0]], np.float32)
    return np.dot(mat_scale, mat_transform)


# Apply rotation to the matrix
def rotateZ(d, mat_transform):
    cos_d = math.cos(d)
    sin_d = math.sin(d)
    mat_rotation_z = np.array([[cos_d, -sin_d, 0.0, 0.0],
                               [sin_d,  cos_d, 0.0, 0.0],
                               [0.0,      0.0, 1.0, 0.0],
                               [0.0,      0.0, 0.0, 1.0]], np.float32)
    return np.dot(mat_rotation_z, mat_transform)
