import pygame
from settings import *
import copy
from collections import deque

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

class GameBoard:
    def __init__(self, window, pacman_initial_pos, ghosts_initial_positions):
        self.window = window
        self.grid = self.create_grid_from_layout(layout)
        self.pacman_position = pacman_initial_pos
        self.ghosts_positions = ghosts_initial_positions
        self.dot = 0

    def create_grid_from_layout(self, layout):
        grid = []
        for row in layout:
            grid_row = []
            for char in row:
                if char == 'W':
                    grid_row.append(HINDERANCE)
                elif char == '.':
                    grid_row.append(DOT)
                else:
                    grid_row.append(EMPTY)
            grid.append(grid_row)
        return grid

    def pacman_caught_by_ghost(self):
        return self.pacman_position in self.ghosts_positions

    def update_pacman_position(self, new_position):
        self.pacman_position = new_position

    def update_ghosts_positions(self, new_positions):
        if isinstance(new_positions, list) and len(new_positions) == 2 and all(isinstance(pos, tuple) and len(pos) == 2 for pos in new_positions):
            self.ghosts_positions = new_positions
        else:
            print(f"Invalid update: {new_positions}. Expected a list of two tuples.")
        
    
    def is_game_over(self):

        return self.pacman_caught_by_ghost() or self.dot ==99

    def draw(self):
        self.window.fill(BLACK)
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == HINDERANCE:
                    pygame.draw.rect(self.window, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif cell == DOT:
                    pygame.draw.circle(self.window, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 10)

        # Draw Pac-Man
        pygame.draw.circle(self.window, YELLOW, (self.pacman_position[0] * CELL_SIZE + CELL_SIZE // 2, self.pacman_position[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

        # Draw Ghosts
        for i, ghost_pos in enumerate(self.ghosts_positions):
            if i == 0: color = RED
            elif i == 1: color = PINK
            pygame.draw.circle(self.window, color, (ghost_pos[0] * CELL_SIZE + CELL_SIZE // 2, ghost_pos[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)
    
    def get_possible_moves(self, is_pacman, ghost_index=None):
        moves = []
        current_pos = self.pacman_position if is_pacman else self.ghosts_positions[ghost_index]

        for m in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dx, dy = m[0], m[1]
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if self.is_valid_position(new_pos):
                moves.append(new_pos)
        
        return moves

    def is_valid_position(self, pos):
        
        x, y = pos
        if 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid):
            return self.grid[y][x] != HINDERANCE
        return False

    def apply_move(self, move, is_pacman, ghost_index=None):

        if is_pacman:
            self.pacman_position = move
            x, y = move

        
            # Check if Pac-Man is on a dot and eat it
            if self.grid[y][x] == DOT:
                self.grid[y][x] = EMPTY
                self.dot +=1


        else:
            self.ghosts_positions[ghost_index] = move



    def clone(self):
        # Create a new GameBoard instance with a copy of the current state
        cloned_board = GameBoard(self.window, self.pacman_position, copy.deepcopy(self.ghosts_positions))
        cloned_board.grid = copy.deepcopy(self.grid)
        cloned_board.dot = self.dot
        return cloned_board
    
    def pacman_position(self):
        return self.pacman_position
    
    def ghosts_positions(self):
        return self.ghosts_positions

    def pacman_ghost_distance(self, ghost_index):
        # Breadth-First Search algorithm to find the shortest path
        start = self.ghosts_positions[ghost_index]
        goal = self.pacman_position
        queue = deque([[start]])
        visited = set()

        while queue:
            path = queue.popleft()
            x, y = path[-1]

            if (x, y) == goal:
                return len(path) - 1  # Subtract 1 to exclude the starting node

            if (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_x, next_y = x + dx, y + dy
                    if self.is_valid_position((next_x, next_y)) and (next_x, next_y) not in visited:
                        new_path = list(path)
                        new_path.append((next_x, next_y))
                        queue.append(new_path)
        print("BFS algo didnt work")
        return float('inf')

