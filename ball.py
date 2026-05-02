#imports
import numpy as np
import pandas as pd
import math
import pygame

#screen resolution variable
x_screen, y_screen = 2400,1080

#display resolution
window = pygame.display.set_mode((x_screen, y_screen))
#gravity
G = 1

class Square:
    def __init__(self, start_position_x, start_position_y, end_position_x, end_position_y, colour):
        self.start_position_x = start_position_x
        self.start_position_y = start_position_y
        self.end_position_x = end_position_x
        self.end_position_y = end_position_y
        self.colour = colour
       
    def render_s(self):
        pygame.draw.line(window, self.colour, (self.start_position_x, self.start_position_y),(self.end_position_x, self.end_position_y),3)
    
    

#class
class Circle:
    def __init__(self, position_x, position_y, speed_x, speed_y, radius, colour):
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.colour = colour

    def render_c(self):
        pygame.draw.circle( window, self.colour, (int(self.position_x), int(self.position_y)), self.radius)

    def speed(self):
        self.position_x += self.speed_x
        self.position_y += self.speed_y

    def wall_collision(self):
        
        #square vectors
        n_upper_left = pygame.math.Vector2(-math.cos(math.radians(45)), -math.                 cos(math.radians(45)))
        n_upper_right = pygame.math.Vector2(math.cos(math.radians(45)), -math.                cos(math.radians(45)))
        n_lower_left = pygame.math.Vector2(-math.cos(math.radians(45)), math.                   cos(math.radians(45)))
        n_lower_right = pygame.math.Vector2(math.cos(math.radians(45)), math.                  cos(math.radians(45)))

        #wall vectors
        n_floor = pygame.math.Vector2(0, -1)
        n_ceiling = pygame.math.Vector2(0, 1)
        n_right = pygame.math.Vector2(-1, 0)
        n_left = pygame.math.Vector2(1, 0)

        #speed to vector
        v = pygame.math.Vector2(self.speed_x, self.speed_y)

        if self.position_x <= self.radius:
            self.position_x = self.radius
            v_reflect = v - 2 * v.dot(n_left) * n_left
            self.speed_x, self.speed_y = v_reflect.x, v_reflect.y
            v = pygame.math.Vector2(self.speed_x, self.speed_y)

        if self.position_x + self.radius >= x_screen:
            self.position_x = x_screen - self.radius
            v_reflect = v - 2 * v.dot(n_right) * n_right
            self.speed_x, self.speed_y = v_reflect.x, v_reflect.y
            v = pygame.math.Vector2(self.speed_x, self.speed_y)

        if self.position_y <= self.radius:
            self.position_y = self.radius
            v_reflect = v - 2 * v.dot(n_ceiling) * n_ceiling
            self.speed_x, self.speed_y = v_reflect.x, v_reflect.y
            v = pygame.math.Vector2(self.speed_x, self.speed_y)

        if self.position_y + self.radius >= y_screen:
            self.position_y = y_screen - self.radius
            v_reflect = v - 2 * v.dot(n_floor) * n_floor
            self.speed_x, self.speed_y = v_reflect.x, v_reflect.y

    def gravity(self):
        if 0 < self.speed_y < 0.1:
            self.speed_y = 0
        else:
            self.speed_y += G

#cirkel
circle_1 = Circle(50, 250, 5, 5, 20, (255,255,255))

#square
line_1 = Square(x_screen/2, y_screen/2, x_screen/2 +60, y_screen/2 +60, (255,255,255))

#initialize pygame
pygame.init()

#naming clock
clock = pygame.time.Clock()



#main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #cleaning screen
    window.fill((0, 0, 0))

    #rendering circle
    circle_1.render_c()
    
    #renering lines
    line_1.render_s()
    
    #calculating gravity
    circle_1.gravity()

    #calculating position
    circle_1.speed()

    #calculating speed after wall collision
    circle_1.wall_collision()

    #renders everything
    pygame.display.flip()

    #frames per second
    clock.tick(120)

pygame.quit()