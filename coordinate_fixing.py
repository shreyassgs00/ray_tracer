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
    return math.degrees(angle)

def place_pixels():
    pixel_plane = []
    for i in range (1,9):
        for j in range (1,7):
            pixel_plane.append([i,j,0])
    return pixel_plane

def eye_to_pixel_vectors(eye,pixel):
    p = np.array(pixel)
    e = np.array(eye)
    return p-e

def make_3d_line(vector,point):
    line = []
    line.append([vector[0],point[0]])
    line.append([vector[1],point[1]])
    line.append([vector[2],point[2]])
    return line
