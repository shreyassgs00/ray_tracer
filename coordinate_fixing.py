import math
import numpy as np
import collections
import conditions

def angle_between_vectors(a1,a2):
    v1  = np.array(a1)
    v2 = np.array(a2)
    normv1 = np.linalg.norm(v1)
    normv2 = np.linalg.norm(v2)
    dot  = np.dot(v1,v2)
    angle = math.acos(dot/(normv1*normv2))
    return angle

def make_3D_line(plane,point):
    return 1

def place_pixels(view_plane,first_pixel):
    return 1
