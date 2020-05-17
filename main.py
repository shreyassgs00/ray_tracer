import coordinate_fixing
import ray_tracer
import conditions
import sys

def main():
    hasFoundError = False

    if not hasFoundError:
        eye = list(map(float, input("Enter the co-ordinates of the eyepoint (Must be in first octet): ").split()))
        if not conditions.verify_first_octet(eye):
            disclaimer = "Eyepoint is not in the first octet. "
            hasFoundError = True

    if not hasFoundError:
        sphere_center = list(map(float, input("Enter the sphere center which is the target (Must be in the fifth octet): ").split()))
        if not conditions.verify_fifth_octet(sphere_center):
            disclaimer = "Sphere center not in the fifth octet. "
            hasFoundError = True

    if not hasFoundError:
        sphere_radius = float(input("Enter the radius of the sphere which is the target: "))
        if not conditions.verify_radius(sphere_center,sphere_radius):
            disclaimer = "Radius not valid as the sphere will intersect the viewport plane."
            hasFoundError = True

    if not hasFoundError:
        source = list(map(float, input("Enter the co-ordinates of the light source: (Must be in the fifth octet) ").split()))
        if not conditions.verify_fifth_octet(source):
            disclaimer = "Source is not in the fifth octet. "
            hasFoundError = True
        elif not conditions.verify_light_source(sphere_center,sphere_radius,source):
            disclaimer = "Source cannot be inside or on the target object. "
            hasFoundError = True
            
    if (hasFoundError):
        return disclaimer
    else:
        return 1
    

if __name__ == '__main__':
    try:
        import numpy as np
        print(main())
    except:
        print("Dependencies not installed. ")