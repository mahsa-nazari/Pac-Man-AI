class GameStateEvaluator:
    def __init__(self):
        # Initialize any necessary attributes or settings
        pass

    def evaluate_state(self, game_board):
        """
        Evaluate the current state of the game board and return a score.
        A higher score typically means a more favorable state for Pac-Man.
        """
        score = 0
        # Example scoring logic: Pac-Man should avoid ghosts
        score -= 5 * self.calculate_pacman_ghost_distance(game_board)
        # Add more scoring logic here based on game state
        return score

    def calculate_pacman_ghost_distance(self, game_board):
        """
        Calculate and return the distance between Pac-Man and the nearest ghost.
        This can be a simple Manhattan distance calculation or more complex logic.
        """
        print('dfgdfgbdfsgsdghsd' , game_board.pacman_position, game_board.ghosts_positions)
        return min(
            [abs(game_board.pacman_position[0] - ghost_pos[0]) 
             + abs(game_board.pacman_position[1] - ghost_pos[1])
             for ghost_pos in game_board.ghosts_positions]
        )
