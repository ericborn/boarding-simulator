# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:39:56 2019

@author: Eric

youtube video that inspired this project
https://www.youtube.com/watch?v=oAHbLRjF0vo
"""

import os, sys
import pandas as pd
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

# setup file location
path = r'C:\Users\Eric\Documents\GitHub\boarding-simulator'
file = 'pass_names'
full_path = os.path.join(path, file + '.csv')

#def simulate(width, row):
#    self.width = width
#    self.row = row
#    self. time = time
#    return('Total time: ' + time)

# row is the total depth of the plane in number of seats
# width is number of seats per side of the plane
# total is (width + width) * row
total_rows = 30
total_width = 6
total_pass = total_width * total_rows

# create list containing all individual seats
seat_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# read csv file into dataframe. Uses the total_pass to only read in the number
# of total passengers for the simulation
try:
    assignments_df = pd.read_csv(full_path, nrows = total_pass)
    print('opened file for passengers: ', file,'\n')

except Exception as e:
    print(e)
    sys.exit('failed to read passenger names')

# list of all possible assignements
assignment_list = []

# Repeats seat letters A through I and row number depending on the size
# of the simulated plane
for i in range(0, total_width):
    for j in range(1, (total_rows + 1)):
        assignment_list.append([j,seat_letters[i]])

# assigns row and seat numbers into the dataframe
for seat in range(0, assignments_df.shape[0]):
    assignments_df['row'][seat] = assignment_list[seat][0]
    assignments_df['seat'][seat] = assignment_list[seat][1]

# determine boarding order
# introduce random delay per person
# calculate delay if person in queue is forced to wait on person taking seat
