import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
import numpy as np
import coordinate_fixing
import math

def plot_diagram(eye,light_source,sphere_center,sphere_radius):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection = '3d')
    
    pixels = coordinate_fixing.place_pixels()
    ax.scatter3D(eye[0],eye[1],eye[2],c='blue')
    ax.scatter3D(light_source[0],light_source[1],light_source[2])

    for i in range (0,len(pixels)):
        x = pixels[i][0]
        y = pixels[i][1]
        z = pixels[i][2]
        ax.scatter3D(x,y,z,c='black')

    ax.scatter3D(sphere_center[0],sphere_center[1],sphere_center[2],c='red')
    u = np.linspace(0,np.pi,100)
    v = np.linspace(0,2*np.pi,100)
    x = sphere_center[0]+sphere_radius*np.outer(np.sin(u), np.sin(v) )
    y = sphere_center[1]+sphere_radius*np.outer(np.sin(u), np.cos(v) )
    z = sphere_center[2]+sphere_radius*np.outer(np.cos(u), np.ones(np.size(v)))
    ax.plot_surface(x,y,z,rstride = 4,cstride = 4,color = 'blue')

    plt.show()
