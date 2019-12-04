# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 06:42:50 2019

@author: Eric
This file will be used to draw the planes cabin, the seats and finally
the passengers moving into the plane and taking their seats
"""
import pygame
from seat import Seat
from random import uniform, randrange #, sample

# define the rows, seats per row and calculate total seats
SEAT_ROWS = 30
SEATS_PER_ROW = 6
TOTAL_SEATS = SEAT_ROWS * SEATS_PER_ROW

# defines the drawing suface size and four fixed RGB colors
# grey, black, red and blue

# fixed drawing surface
#WIDTH = 1200
#HEIGHT = 400

# dynamic drawing surface
WIDTH = SEAT_ROWS * 40
HEIGHT = SEATS_PER_ROW * 65

GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (215, 0, 0)
BLUE = (0, 0, 215)
ORANGE = (255, 145, 25)
LIGHT_BLUE = (90, 200, 215)

# test coords
#coords = [[50, 50], [50, 100], [50, 150], [100, 50], [100, 100], [100, 150]]

# creates a list to store the coordinates for the seats, where passengers
# will end up and the start where they will line up
seat_coords = []
end_coords = []
start_coords = []

# top left of aisle
aisle_start = [115, 180]

# iterates through the total number of rows and seats per row to generate the 
# coordinates where the seat will be drawn, the ending coords represents the 
# locations the passengers will end up

# bottom left edge of seats 115, 250
for i in range(1, SEAT_ROWS + 1):
    seat_x = (i * 30) + 100
  
    for j in range(1, SEATS_PER_ROW + 1):        
        # top 3 rows of seats
        if j < 4:
            seat_y = (j * 20) + 100

        # bottom 3 rows of seats with a gap of 20 pixels
        if j > 3:
            seat_y = (j * 20) + 120

        # appends the coords to each list
        seat_coords.append([seat_x, seat_y])
        end_coords.append([seat_x + 2.5, seat_x + 3.1])

# loop below generates the start coords which represents where the passengers  
# will be in the queue entering the plane.
# starting queue x coords
start_x = 115  
     
for k in range(1, TOTAL_SEATS + 1):
    #print(k)
    # starting queue y coords
    start_y = (k * 12.5) + 250
    start_coords.append([start_x, start_y])

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Boarding Simulator')
clock = pygame.time.Clock()

class Passenger(Seat):
    
    # overrides the color and size from Seat
    def __init__(self):
        Seat.__init__(self, (255, 145, 25), 10)
        self.x = 0
        self.y = 0
    # function that makes a check, if another passenger is in the space
    # where it needs to move next, the current passenger stops
    def queue(self, other_passenger):
        if other_passenger.present == True:
            self.stop = True

#    def move(self):
#        self.move_on_x = randrange(0, 2)
#        self.move_on_y = randrange(0, 2)
#        self.x += self.move_on_x
#        self.y += self.move_on_y
    
    # random step distance
    def move_x(self):
        self.move_on_x = randrange(0, 2)
        self.x += self.move_on_x
        
    def move_y(self):
        self.move_on_y = randrange(0, 2)
        self.y += self.move_on_y
        
#def is_touching(self, other_passenger):

# creates the visual environment
def draw_environment(seat_list, start_list):
    # fills the background with white
    game_display.fill(GREY)
    
    # iterates creating seats for each passed in from the seat_list
    for seat_dict in seat_list:
        for seat_id in seat_dict:
            seat = seat_dict[seat_id]
            
            # iterates through the coords list using seat_id as the index
            seat_x = seat_coords[seat_id][0]
            seat_y = seat_coords[seat_id][1]
            
            # tuple represents x, y, width, height
            pygame.draw.rect(game_display, seat.color, (seat_x, seat_y,
                                                        seat.size, seat.size))

    # iterates creating passengers in their queue position
    for pass_dict in start_list:
        for pass_id in pass_dict:
            passenger = pass_dict[pass_id]
            
            # TODO
            # THIS IS CAUSING THE PASSENGERS TO BECOME FIXED IN PLACE
            # NEED A NEW METHOD TO ASSIGN THEM TO THEIR LOCATION BEFORE STARTING THE MOTION
            # iterates through the coords list using pass_id as the index
#            pass_x = start_coords[pass_id][0]
#            pass_y = start_coords[pass_id][1]
            
#            passenger.x = start_coords[pass_id][0]
#            passenger.y = start_coords[pass_id][1]
            
            #print(pass_x, pass_y)
            
            # tuple represents x, y, width, height
            pygame.draw.rect(game_display, passenger.color, (passenger.x,
                                                             passenger.y,
                                                             passenger.size,
                                                             passenger.size))
            if 
            passenger.move_x()
            passenger.move_y()
#            passenger.move()

    # updates the game display, drawing all of the objects 
    pygame.display.update()

def main():
    #blue_seat = Seat(color=BLUE)
    blue_seats = dict(enumerate([Seat(BLUE, 15) for i in range(TOTAL_SEATS)]))
    passengers = dict(enumerate([Passenger() for i in range(TOTAL_SEATS)]))
    #print(passengers)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([blue_seats], [passengers])
        clock.tick(60)

if __name__ == '__main__':
    main()