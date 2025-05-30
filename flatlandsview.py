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

    