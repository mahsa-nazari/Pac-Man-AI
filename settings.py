# settings.py
# Game configuration settings

# Define the size of each cell in the grid
CELL_SIZE = 20  # pixels

# Colors used in the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
PINK = (255, 105, 180)

# Screen dimensions based on the grid size
GRID_WIDTH = 20
GRID_HEIGHT = 11
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT