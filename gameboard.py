import pygame
from settings import *

# Define grid values
EMPTY = 0
DOT = 1
HINDERANCE = 2
PACMAN = 3
GHOST = 4

# This layout defines the positions of walls (W), Pacman (P), Ghosts (G), and dots (.).

layout = [
    "WWWWWWWWWWWWWWWWWWWW", #0
    "W....W........W....W", #1
    "W.WW.W.WWWWWW.W.WW.W", #2
    "W.W..............W.W", #3
    "W.W.WW.WW  WW.WW.W.W", #4
    "W......W    W......W", #5
    "W.W.WW.WWWWWW.WW.W.W", #6
    "W.W....... ......W.W", #7
    "W.WW.W.WWWWWW.W.WW.W",  #8
    "W....W........W....W", #9
    "WWWWWWWWWWWWWWWWWWWW"  #10
]
for i in range(len(layout)): print(i, len(layout[i]))
class GameBoard:
    def __init__(self, window):
        self.window = window
        self.grid = self.create_grid_from_layout(layout)

    def create_grid_from_layout(self, layout):
        grid = []
        for row in layout:
            grid_row = []
            for char in row:
                if char == 'W':
                    grid_row.append(HINDERANCE)
                elif char == '.':
                    grid_row.append(DOT)
                elif char == 'P':
                    grid_row.append(PACMAN)
                elif char == 'G':
                    grid_row.append(GHOST)
                else:
                    grid_row.append(EMPTY)
            grid.append(grid_row)
        return grid

    def draw(self):
        self.window.fill(BLACK)  # Fill the background with black
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == HINDERANCE:
                    # Draw walls as blue rectangles
                    pygame.draw.rect(self.window, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif cell == DOT:
                    # Draw dots as small white circles
                    pygame.draw.circle(self.window, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 10)