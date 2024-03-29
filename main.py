# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:39:56 2019

@author: Eric

youtube video that inspired this project
https://www.youtube.com/watch?v=oAHbLRjF0vo
"""

import math
import os, sys
import pandas as pd
from random import uniform, sample

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
path = r'C:\Code projects\git projects\boarding-simulator'
file = 'pass_names'
full_path = os.path.join(path, file + '.csv')

#def simulate(width, row):
## checks for rows between 20-35
#if total_rows > 19 and total_rows < 36:
#    pass
#else:
#    print('Please provide a row count between 20 and 35')

## checks for width between 3-9
#if total_width > 2 and total_width < 10:
#    pass
#else:
#    print('Please provide a width between 3 and 9 seats')

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

# 35" for each row
# human step average 30"
row_length = 35
step_length = 30

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

# randomly sorts the entire seat order with no repeated elements
order = sample(range(0, len(assignment_list)), len(assignment_list))


time_list = []

for i in range(0, 1001):

    # initlialize total time
    no_delay_time = 0
    
    # iterate through all passengers and calculate time. Does nor include any delay
    # for stowing/sitting or being queued behind someone
    for people in order:
        # rounds up the number of steps needed to reach the seat position
        total_steps = math.ceil(((assignments_df['row'][order[people]]) * row_length) / step_length)
        
        # random time it takes to step
        step_duration = uniform(0.3, 1.5)
        
        # total time added from each passenger
        no_delay_time += round((total_steps * step_duration))
    
    # print time with no deplay's
    #print(round((no_delay_time / 60),2))
    
    # stowing/sitting delay
    sitting_time = 0
    
    # delayed time
    for people in order:
        # rounds up the number of steps needed to reach the seat position
        total_steps = math.ceil(((assignments_df['row'][order[people]]) * row_length) / step_length)
        
        # random time it takes to step
        step_duration = uniform(0.3, 1.5)
        
        if assignments_df['seat'][order[people]] == 'C' or assignments_df['seat'][order[people]] == 'F':
            # random time for stowing/sitting
            sit_duration = uniform(0.5, 2)
            
        if assignments_df['seat'][order[people]] == 'B' or assignments_df['seat'][order[people]] == 'E':
            # random time for stowing/sitting
            sit_duration = uniform(0.3, 1.5)
    
        if assignments_df['seat'][order[people]] == 'A' or assignments_df['seat'][order[people]] == 'D':
            # random time for stowing/sitting
            sit_duration = uniform(0.2, 1.0)
            
        # total time added from each passenger
        sitting_time += round(((total_steps * step_duration) + sit_duration))
        
    # print time with no deplay's
    #print(round((sitting_time / 60),2))
    time_list.append([round((no_delay_time / 60),2), round((sitting_time / 60),2)])
    
print(time_list)

# initialize for average times
no_delay_average = 0
sitting_time_average = 0

# add up each of the times for the respective
for i in range(0, len(time_list)):
    no_delay_average += time_list[i][0]
    sitting_time_average += time_list[i][1]

no_delay_average = round((no_delay_average / len(time_list)),2)
sitting_time_average = round((sitting_time_average / len(time_list)),2)

print('No delay average:', no_delay_average,
      '\nSitting time average', sitting_time_average)