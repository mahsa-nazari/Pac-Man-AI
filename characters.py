import pygame
from settings import *

class Character:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 2)

class Pacman(Character):
    def __init__(self, x, y):
        super().__init__(x, y, YELLOW)
    
class Ghost(Character):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

