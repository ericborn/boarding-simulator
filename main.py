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

def simulate(width, row):
    self.width = width
    self.row = row
    self. time = time
    return('Total time: ' + time)

# row is the total depth of the plane in number of seats
# width is number of seats per side of the plane
# total is (width + width) * row
total_rows = 30
total_width = 6
total_pass = width * rows

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

# fills assignments list
for i in range(0, total_width):
    #print(seat_letters[i])
    for j in range(1, (total_rows + 1)):
        assignment_list.append([j,seat_letters[i]])

# access index 0 from assignements df
assignments_df['name'][0]
#assignments_df['row'] = 

# seat assignemts is a dictionary containing sequential numbers from 1..x
# where x represents the highest numbered passenger on the plane.
# assignents
seat_assignments = {}

for i in range(1, total):
    print(i)
    seat_assignments
    # assign key as i
    