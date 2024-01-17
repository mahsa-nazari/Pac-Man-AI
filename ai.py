class GameAI:
    def __init__(self, max_depth, state_evaluator):
        self.max_depth = max_depth
        self.state_evaluator = state_evaluator  # Instance of GameStateEvaluator

    def minimax(self, game_board, depth, alpha, beta, maximizing_player):
        # Unchanged
        if depth == 0 or self.game_over(game_board):
            return self.state_evaluator.evaluate_state(game_board), None

        if maximizing_player:
            return self.maximize(game_board, depth, alpha, beta)
        else:
            return self.minimize(game_board, depth, alpha, beta)

    def maximize(self, game_board, depth, alpha, beta):
        max_eval = float('-inf')  # Start with the lowest possible evaluation
        best_move = None

        for move in self.get_possible_moves(game_board, True):  # True for Pacman
            new_board = game_board.clone()
            new_board.apply_move(move, True)  # Apply Pac-Man's move

            eval, _ = self.minimax(new_board, depth - 1, alpha, beta, False)  # Minimize for ghosts in the next level
            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)  # Update alpha
            if beta <= alpha:
                break  # Alpha-Beta pruning

        return max_eval, best_move

    def minimize(self, game_board, depth, alpha, beta):
        min_eval = beta
        best_move = None
        for ghost_index in range(2):
            for move in self.get_possible_moves(game_board, False, ghost_index):  # False for Ghosts
                new_board = game_board.clone()
                new_board.apply_move(move, False, ghost_index)
                eval, _ = self.minimax(new_board, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha-Beta pruning
        return min_eval, best_move

    def get_possible_moves(self, game_board, is_pacman, ghost_index=None):
        return game_board.get_possible_moves(is_pacman, ghost_index)

    def game_over(self, game_board):
        return game_board.is_game_over()

    


