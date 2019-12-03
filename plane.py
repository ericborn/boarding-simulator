# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 06:42:50 2019

@author: Eric
This file will be used to draw the planes cabin, the seats and finally
the passengers moving into the plane and taking their seats
"""
import pygame
#from seat import seat

# define the rows, seats per row and calculate total seats
SEAT_ROWS = 30
SEATS_PER_ROW = 6
TOTAL_SEATS = SEAT_ROWS * SEATS_PER_ROW
#TOTAL_SEATS = 80

# defines the drawing suface size and four fixed RGB colors
# white, black, red and blue
WIDTH = 1920
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# test coords
#coords = [[50, 50], [50, 100], [50, 150], [100, 50], [100, 100], [100, 150]]

# creates a list to store the coordinates for the seats
coords = []

# iterates through the total number of rows and seats per row multiplying
# each by 50 to move the pixels for the seats 50 apart
for i in range(1, SEAT_ROWS + 1):
    x = i * 30
    for j in range(1, SEATS_PER_ROW + 1):
        y = j * 20
        #print(x, y)
        coords.append([x, y])

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Boarding Simulator')
clock = pygame.time.Clock()

# seat class
class Seat:
    # init method is run when seat classes are initialized
    # self allows you to set variables that the class always starts with
    def __init__(self, color):
        
        # x coordinate
        self.x = 50
        
        # y coordinate
        self.y = 50
        
        # used for both width and height since we want a square
        self.size = 10
        
        # starting color
        self.color = color

# creates the visual environment
def draw_environment(seat_list):
    # fills the background with white
    game_display.fill(WHITE)
    
    # iterates creating seats for each passed in from the seat_list
    for seat_dict in seat_list:
        for seat_id in seat_dict:
            seat = seat_dict[seat_id]
            #new_x = seat.x * seat_id
            #new_y = seat.x * seat_id
            new_x = coords[seat_id][0]
            new_y = coords[seat_id][1]
            pygame.draw.rect(game_display, seat.color, (new_x, new_y, seat.size, seat.size))

    # tuple represents x, y, width, height
    #pygame.draw.rect(game_display, seat.color, (seat.x, seat.y, seat.size, seat.size))
    
    # updates the game display, drawing all of the objects 
    pygame.display.update()

def main():
    #blue_seat = Seat(color=BLUE)
    blue_seats = dict(enumerate([Seat(BLUE) for i in range(TOTAL_SEATS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([blue_seats])
        clock.tick(60)

if __name__ == '__main__':
    main()