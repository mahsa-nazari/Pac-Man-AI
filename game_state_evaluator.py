
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
        distances = []
        for ghost_pos in game_board.ghosts_positions:
            # Ensure ghost_pos is a tuple or list
            if isinstance(ghost_pos, (tuple, list)) and len(ghost_pos) == 2:
                distance = abs(game_board.pacman_position[0] - ghost_pos[0]) + \
                           abs(game_board.pacman_position[1] - ghost_pos[1])
                distances.append(distance)
            else:
                print(f"Invalid ghost position: {ghost_pos}")
        return min(distances) if distances else 0