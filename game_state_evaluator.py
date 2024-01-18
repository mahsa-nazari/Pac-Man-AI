class GameStateEvaluator:
    def __init__(self):
        self.loss = 0

    def evaluate_state(self, game_board):
        """
        Evaluate the current state of the game board and return a loss.
        A higher loss typically means a more favorable state for Pac-Man.
        """
        # Example scoring logic: Pac-Man should avoid ghosts
        self.loss = 0
        distances = (game_board.pacman_ghost_distance(0), game_board.pacman_ghost_distance(1))
        self.min_distance = min(distances)
        loss_multiplier = 100  # Adjust this multiplier as needed
        self.loss = loss_multiplier / (self.min_distance + 1)  # +1 to avoid division by zero
        return 1/self.loss

    
    def print_losses(self):
        print("loss: ", self.loss, "score: ", 1/ self.loss, "minimun distance", self.min_distance)
