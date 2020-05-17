import numpy as np 
import math
import collections

def compare(a1, a2):
    if (a1 == a2):
        return True
    else:
        return False
    
def verify_distance(eye,target,viewport_distance):
    e = np.array(eye)
    t = np.array(target)
    d = np.linalg.norm(e-t)
    if (d>viewport_distance):
        return False
    else:
        return True

def verify_plane_point(plane,point):
    a = point[0]
    b = point[1]
    c = point[2]
    A = plane[0]
    B = plane[1]
    C = plane[2]
    D = plane[3]
    if (((A*a)+(B*b)+(c*C)+D) == 0):
        return False
    else:
        return True

def verify_first_octet(point):
    x = point[0]
    y = point[1]
    z = point[2]
    if (x>0 and y>0 and z>0):
        return True
    else:
        return False 

def verify_fifth_octet(point):
    x = point[0]
    y = point[1]
    z = point[2]
    if (x>0 and y>0 and z<0):
        return True
    else:
        return False

def verify_radius(center,radius):
    c = np.array(center)
    normal_point = [center[0],center[1],0]
    n = np.array(normal_point)
    if np.linalg.norm(c-n)>radius:
        return True
    else:
        return False

def verify_light_source(center,radius,source):
    x = source[0]-center[0]
    y = source[1]-center[1]
    z = source[2]-center[2]
    r = radius
    value = math.pow(x,2)+math.pow(y,2)+math.pow(z,2)-math.pow(r,2)
    if value>0:
        return True
    else:
        return False
