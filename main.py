# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:39:56 2019

@author: Eric

youtube video that inspired this project
https://www.youtube.com/watch?v=oAHbLRjF0vo
"""
from random import random

# setup function that takes number of seats per row and total rows
# optional method used to assign seats to passengers, can be random if not specified
# outputs time to fill the seats

# develop methods of assignment
# random, back to front, front to back, one side then other back to front, 
# window then middle then isle

# random needs to be included in the time delay between reaching seat and sitting down
# next passenger cannot move forward until previous is seated
# add time delay if passengers seat is blocked by other passengers already seated


def simulate(width, row):
    self.width = width
    self.row = row
    self. time = time
    return('Total time: ' + time)

# row is the total depth of the plane in number of seats
# width is number of seats per side of the plane
# total is (width + width) * row
row = 30
width = 3
total = (width + width) * row

# seat assignemts is a dictionary containing sequential numbers from 1..x
# where x represents the highest numbered passenger on the plane.
# assignents
seat_assignments = {}