# pacman.py
import pygame
from settings import *

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = PACMAN_SPEED
        self.image = pygame.image.load(PACMAN_IMAGE)
        self.image = pygame.transform.scale(self.image, (GRID_SIZE, GRID_SIZE))
        
    def move(self, dx, dy, maze):
        new_x = self.x + dx
        new_y = self.y + dy
        
        if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze):
            if maze[int(new_y)][int(new_x)] != "#":
                self.x = new_x
                self.y = new_y
                
    def draw(self, win, offset_x=0, offset_y=0):
        win.blit(self.image, (self.x * GRID_SIZE + offset_x, self.y * GRID_SIZE + offset_y))
        
    def get_pos(self):
        return (int(self.x), int(self.y))