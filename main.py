import coordinate_fixing
import ray_tracer
import conditions
import sys
import plot_diagram

def main():
    hasFoundError = False
    eye = []
    sphere_center = []
    source = []
    sphere_radius = 0

    if not hasFoundError:
        eye = list(map(float, input("Enter the co-ordinates of the eyepoint (Must be in  z-positive octant): ").split()))
        if not conditions.verify_zpos_octant(eye):
            disclaimer = "Eyepoint is not in the z-positive octant octant. "
            hasFoundError = True

    if not hasFoundError:
        sphere_center = list(map(float, input("Enter the sphere center which is the target (Must be in z-negative octant): ").split()))
        if not conditions.verify_zneg_octant(sphere_center):
            disclaimer = "Sphere center not in the z-negative octant. "
            hasFoundError = True

    if not hasFoundError:
        sphere_radius = float(input("Enter the radius of the sphere which is the target: "))
        if not conditions.verify_radius(sphere_center,sphere_radius):
            disclaimer = "Radius not valid as the sphere will intersect the viewport plane."
            hasFoundError = True

    if not hasFoundError:
        source = list(map(float, input("Enter the co-ordinates of the light source: (Must be in z-negative octant) ").split()))
        if not conditions.verify_zneg_octant(source):
            disclaimer = "Source is not in the z-negative octant. "
            hasFoundError = True
        elif not conditions.verify_light_source(sphere_center,sphere_radius,source):
            disclaimer = "Source cannot be inside or on the target object. "
            hasFoundError = True
            
    if (hasFoundError):
        return disclaimer
    else:
        disclaimer = "Considering the viewport plane is the positive x-y plane which contains 48 pixels at a unit distance from each other, the results are displayed. "
        pixels = coordinate_fixing.place_pixels()
        angles = [] 
        reflected_lines = []
        for i in range (0, len(pixels)):
            pixel = pixels[i]
            vector = coordinate_fixing.eye_to_pixel_vectors(eye,pixel)
            line = coordinate_fixing.make_3d_line(vector,eye)
            intersection = ray_tracer.find_interesection(line,sphere_center,sphere_radius)

            if intersection!=0:
                normal = ray_tracer.normal_from_center(sphere_center,intersection)
                angle = coordinate_fixing.angle_between_vectors(vector,normal)
                angle = 180 - angle
                angles.append(angle)
                
                reflected_line = ray_tracer.find_reflected_line(normal,intersection,angle)
                reflected_lines.append(reflected_line)
            else:
                continue
    plot_diagram.plot_diagram(eye,source,sphere_center,sphere_radius)
    return reflected_lines

if __name__ == '__main__':
    try:
        import matplotlib.pyplot as plt
        from mpl_toolkits import mplot3d
        import numpy as np
        print(main())
    except:
        print("Dependencies not installed. ")