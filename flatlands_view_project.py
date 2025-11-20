# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:12:21 2025

@author: julia
"""

import numpy as np
import matplotlib.pyplot as plt

def Generate_Polygon(n):
    """
    Generates and plots points of a n-sided polygon.
    n should be a positive integer.
    """
    #Create an array for the x and y coordinates of each point
    points = np.zeros((n,2))
    
    #Create the points for the polygon and add them to the array
    for i in range(n):
        points[i] = [np.cos(i*2*np.pi/n),np.sin(i*2*np.pi/n)]
    
    #Plot out the polygon
    polygon = plt.Polygon(points, closed=True, edgecolor='black', facecolor='lightblue')
    plt.gca().add_patch(polygon)
    
    #Set limits of the graph
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    
    #Make the graph not looked squished - even out graph axis
    plt.gca().set_aspect('equal')
    
    return points

def Flatlands_View(n):
    
    #Call the polygon vertices
    polygon_points = Generate_Polygon(n)
    
    #Find which coordinates lie in the x>0 plane
    visible_vertices = []
    
    for i in range(len(polygon_points)):
        if polygon_points[i][0] >= -1e-10:
            visible_vertices.append(tuple(polygon_points[i]))
    
    #Order by y value
    sorted_visible_vertices = sorted(visible_vertices, key=lambda tup: tup[1])
    
    #Create points on the x = 2 axis to analyse
    # x_2_axis = np.zeros((100,2))
    
    #Create interpolation for each vertex
    x = []
    # y = []
    
    for i in range(len(sorted_visible_vertices)-1):
        x_values = np.linspace(sorted_visible_vertices[i][0], sorted_visible_vertices[i+1][0], 10)
        # y_values = np.linspace(sorted_visible_vertices[i][1], sorted_visible_vertices[i+1][1], 10)
        
        #Make sure there are no duplicates
        if i == 0:
            x.extend(x_values)
            # y.extend(y_values)
        
        else:
            x.extend(x_values[1:])
            # y.extend(y_values[1:])
            
    return x

#30/05/2025 18:02 Added to github

def Generate_Polygon_2(n):
    """
    Generates and plots points of a n-sided polygon.
    n should be a positive integer.
    """
    #Create an array for the x and y coordinates of each point
    points = np.zeros((n+1,2))
    
    #Create the points for the polygon and add them to the array
    for i in range(n+1):
        points[i] = [np.cos(i*2*np.pi/n),np.sin(i*2*np.pi/n)]
    
    # #Plot out the polygon
    # polygon = plt.Polygon(points, closed=True, edgecolor='black', facecolor='lightblue')
    # plt.gca().add_patch(polygon)
    
    # #Set limits of the graph
    # plt.xlim(-1.5,1.5)
    # plt.ylim(-1.5,1.5)
    
    # #Make the graph not looked squished - even out graph axis
    # plt.gca().set_aspect('equal')
    
    return points

def Flatlands_View_2(n,d):
        
    #Call the polygon vertices
    polygon_points = Generate_Polygon_2(n)
    
    #Create a list of all the visible values
    x = []
    y = []
    
    for i in range(len(polygon_points)-1):
        x_values = np.linspace(polygon_points[i][0], polygon_points[i+1][0], d)
        y_values = np.linspace(polygon_points[i][1], polygon_points[i+1][1], d)
            
        #Make sure there are no duplicates
        if i == 0:
            x.extend(x_values)
            y.extend(y_values)
            
        elif i == len(polygon_points) - 2:
            x.extend(x_values[1:d-1])
            y.extend(y_values[1:d-1])
            
        else:
            x.extend(x_values[1:])
            y.extend(y_values[1:])
            
    #Find points beyond x=0
    x_pos = []
    y_pos = []
        
    for i in range(len(x)):
        if x[i] > -1e-10:
            x_pos.append(x[i])
            y_pos.append(y[i])
            
    #Find all visible points from reference x=1
    x_visible = []
    y_visible = []
    max_y_index = np.argmax(y_pos)
    
    for i in range(len(x_pos)):
        if x_pos[i] >= x_pos[max_y_index] - 1e-10:
            x_visible.append(x_pos[i])
            y_visible.append(y_pos[i])
    
    #Sort points in order of y value
    x_visible_sorted = []
    y_visible_sorted = []
    
    for i in range(len(x_visible)):
        x_visible_sorted.append(x_visible[np.argsort(y_visible)[i]])
        y_visible_sorted.append(y_visible[np.argsort(y_visible)[i]])
    
     # for i in range(len(x_visible)):
         
     #     index = np.argsort(y_visible)[i]
     #     x_val = x_visible[index]
     #     y_val = y_visible[index]
         
     #     if i == 0:
     #         x_visible_sorted.append(x_val)
     #         y_visible_sorted.append(y_val)
         
     #     else:
     #         if abs(x_visible_sorted[i-1] -  x_visible[np.argsort(y_visible)[i]]) > 1e-10:
     #             x_visible_sorted.append(x_visible[np.argsort(y_visible)[i]])
     #             y_visible_sorted.append(y_visible[np.argsort(y_visible)[i]])
    
    x_distance = np.array(x_visible_sorted).reshape(1,len(x_visible_sorted))
    plt.imshow(x_distance, cmap = 'coolwarm')
    plt.colorbar()
    plt.gca().set_aspect('auto')
    plt.show()
                
    return x_visible_sorted, y_visible_sorted

#Could change 1e-10 to a smaller number if dealing with a polygon of great order.
#Could change 10 into variable
            
        