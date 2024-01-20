from unittest import TestCase
from gameboard import GameBoard, HINDERANCE, DOT, EMPTY, CELL_SIZE, BLUE, WHITE, YELLOW, RED  # Replace 'your_game_file' with the actual file name
import copy
from collections import deque

class TestGame(TestCase):
    def setUp(self):
        # Dummy window for testing
        self.window = None  
        # Sample layout for testing
        self.layout = [
            "WWWWW",
            "W...W",
            "W...W",
            "WWWWW"
        ]
        self.pacman_initial_pos = (1, 1)
        self.ghosts_initial_positions = [(4, 1), (4, 2)]
        self.game_board = GameBoard(self.window, self.pacman_initial_pos, 
                                    self.ghosts_initial_positions)

    def test_create_grid_from_layout(self):
        """Test if grid is correct"""
        grid = [
                    [HINDERANCE, HINDERANCE,HINDERANCE, HINDERANCE, HINDERANCE],
                    [HINDERANCE, DOT, DOT, DOT, HINDERANCE],
                    [HINDERANCE, DOT, DOT, DOT, HINDERANCE],
                    [HINDERANCE, HINDERANCE,HINDERANCE, HINDERANCE, HINDERANCE]
                ]
        self.assertEqual(self.game_board.create_grid_from_layout(self.layout), grid)



