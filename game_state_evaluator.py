
class GameStateEvaluator:
    def __init__(self):
        # Initialize any necessary attributes or settings
        pass

    def evaluate_state(self, game_board):
        """
        Evaluate the current state of the game board and return a score.
        A higher score typically means a more favorable state for Pac-Man.
        """
        # Example scoring logic: Pac-Man should avoid ghosts
        try:
            score -= 5 * self.calculate_pacman_ghost_distance(game_board)
        except: score = 0 - 5 * self.calculate_pacman_ghost_distance(game_board)
        # Add more scoring logic here based on game state
        return score

    def calculate_pacman_ghost_distance(self, game_board):
        distances = []
        print('game_board.ghosts_positions', game_board.ghosts_positions)
        for ghost_pos in game_board.ghosts_positions:
            distance = abs(game_board.pacman_position[0] - ghost_pos[0]) + abs(game_board.pacman_position[1] - ghost_pos[1])
            distances.append(distance)
            print('distances',distances)

        return min(distances) if distances else 0