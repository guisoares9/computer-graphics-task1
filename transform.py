import numpy as np
import math

class Transform:

    def rotateZ(d, mat_transform):
        cos_d = math.cos(d)
        sin_d = math.sin(d)
        mat_rotation_z = np.array([[cos_d, -sin_d, 0.0, 0.0], 
                                    [sin_d,  cos_d, 0.0, 0.0], 
                                    [0.0,      0.0, 1.0, 0.0], 
                                    [0.0,      0.0, 0.0, 1.0]], np.float32)
        return np.dot(mat_rotation_z, mat_transform)

    def rotateX(d, mat_transform):
        cos_d = math.cos(d)
        sin_d = math.sin(d)
        mat_rotation_x = np.array([[1.0,   0.0,    0.0, 0.0], 
                                    [0.0, cos_d, -sin_d, 0.0], 
                                    [0.0, sin_d,  cos_d, 0.0], 
                                    [0.0,   0.0,    0.0, 1.0]], np.float32)
        return np.dot(mat_rotation_x, mat_transform)

    def rotateY(d, mat_transform):
        cos_d = math.cos(d)
        sin_d = math.sin(d)
        mat_rotation_y = np.array([[cos_d,  0.0, sin_d, 0.0], 
                                    [0.0,    1.0,   0.0, 0.0], 
                                    [-sin_d, 0.0, cos_d, 0.0], 
                                    [0.0,    0.0,   0.0, 1.0]], np.float32)
        
        return np.dot(mat_rotation_y, mat_transform)