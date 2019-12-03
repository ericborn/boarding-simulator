# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 06:59:41 2019

@author: Eric
Defines the seat starting size, x/y position and color
"""
# seat class
class Seat:
    # init method is run when seat classes are initialized
    # self allows you to set variables that the class always starts with
    def __init__(self, color, size):
    #def __init__(self, color, x_bound, y_bound):

        # define the x/y boundaries
#        self.x_bound = x_bound
#        self.y_bound = y_bound
        
        # starting color
        self.color = color
        
        # used for both width and height since we want a square
        self.size = size