import math
import cmath
import numpy as np
import collections
import conditions
import coordinate_fixing

def solve_quad(a,b,c):
    d = (b**2)-(4*a*c)
    solution = [0,0]
    solution[0] = ((-b)-(cmath.sqrt(d)))/(2*a)
    solution[1] = ((-b)+(cmath.sqrt(d)))/(2*a)
    if (solution[0].imag == 0 and solution[1].imag == 0):
        return solution
    else:
        return 0

def find_interesection(line,sphere_center,sphere_radius):
    equation = []
    for i in range (0,3):
        equation.append([line[i][0],line[i][1]-sphere_center[i]])
    quad_equation = []
    for i in range (0,3):
        quad_equation.append([math.pow(equation[i][0],2),2*equation[i][0]*equation[i][1],math.pow(equation[i][1],2)])
    
    final_equation = []
    final_equation.append(quad_equation[0][0]+quad_equation[1][0]+quad_equation[2][0])
    final_equation.append(quad_equation[0][1]+quad_equation[1][1]+quad_equation[2][1])
    final_equation.append(quad_equation[0][2]+quad_equation[1][2]+quad_equation[2][2]-math.pow(sphere_radius,2))
    
    parameter_for_intersection = solve_quad(final_equation[0],final_equation[1],final_equation[2])
    intersection_point = []
    if (parameter_for_intersection!=0):
        x = 0
        y = 0
        z = 0
        compare = []
        for i in range (0,len(parameter_for_intersection)):
            x = line[0][0]*parameter_for_intersection[i] + line[0][1]
            y = line[1][0]*parameter_for_intersection[i] + line[1][1]
            z = line[2][0]*parameter_for_intersection[i] + line[2][1]
            compare.append([x,y,z])
        normal_points = []
        for i in range (0,len(compare)):
            normal_points.append([compare[i][0],compare[i][1],0])
        if np.linalg.norm(np.array(compare[0])-np.array(normal_points[0])) > np.linalg.norm(np.array(compare[1])-np.array(normal_points[1])):
            intersection_point = compare[1]
            return intersection_point
        else:
            intersection_point = compare[0]
            return intersection_point
    else:
        return 0

def normal_from_center(center,intersection_point):
    c = np.array(center)
    i = np.array(intersection_point)
    normal = i-c
    return normal

def find_reflected_line(normal,intersection_point,angle):
    reflected_ray = [0,0,0]
    for i in range (0,len(normal)):
        reflected_ray[i] = (normal[i]/math.cos(angle)) 
    reflected_line = []
    for j in range(0,len(reflected_ray)):
        reflected_line.append([reflected_ray[j],intersection_point[j]])
    return reflected_line
