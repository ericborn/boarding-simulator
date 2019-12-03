# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 06:42:50 2019

@author: Eric
This file will be used to draw the planes cabin, the seats and finally
the passengers moving into the plane and taking their seats
"""
import pygame

# define the rows, seats per row and calculate total seats
seat_rows = 30
seats_per_row = 6
total_seats = seat_rows * seats_per_row

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Boarding Simulator')
clock = pygame.time.Clock()

# class
class Seat:
    # init method is run when seat classes are initialized
    # self allows you to set variables that the class always starts with
    def __init__(self, color):
        self.x = 50
        self.y = 50
        self.size = 5
        self.color = color

def draw_environment(seat):
    game_display.fill(WHITE)
    pygame.draw.circle(game_display, seat.color, [seat.x, seat.y], seat.size)
    pygame.display.update()

def main():
    blue_seat = Seat(color=BLUE)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(blue_seat)
        clock.tick(60)

if __name__ == '__main__':
    main()