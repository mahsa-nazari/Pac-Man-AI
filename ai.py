import random

pacman_position_history = [(10,7)]
class GameAI:
    def __init__(self, v=True):

        self.v = v


    def minimax(self, game_board, depth, alpha, beta, maximizing_player):
        self.possible_moves = self.get_possible_moves(game_board, True)
        self.depth = depth
        if depth == 0 or self.game_over(game_board):
            return self.evaluate_state(game_board, maximizing_player), None

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
        min_eval = float('inf')
        best_move = None
        for ghost_index in range(2):
            for move in game_board.get_possible_moves(False, ghost_index):  # False for Ghosts
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
    
    def evaluate_state(self, game_board, v=True):
        global pacman_position_history
        """
        Evaluate the current state of the game board and return a score.
        A higher score means a more favorable state for Pac-Man.
        """
        pacman_position = game_board.pacman_position
        
        self.score = 0
        if pacman_position in [(11, 5), (8, 5)]: 
            self.score -= 10

        # Pac-Man should avoid ghosts
        distances = (game_board.pacman_ghost_distance(0), game_board.pacman_ghost_distance(1))
        self.min_distance = min(distances)
        m = 10
        self.n = 10
        #import dot eatign score from board
        self.dot = game_board.dot
        #Higher exploration score for end of the game
        if self.dot > 70: self.n = 20
        self.possible_moves = game_board.get_possible_moves(True)

        # different pathes can lead to identical score and this will prevent pacman form moving forward, the issue got fixed by
        #adding a small random component can improve the process of decision making by adding variability witohut changing the overall outcome 
        self.score = m * self.dot + 2*random.random()

        # Higher score for not recursive movements due to more exploration
        # higher exploration through the end of the game when pacman in possibly not close to dots anymore
        if pacman_position not in pacman_position_history: self.score +=self.n
        pacman_position_history = game_board.update_pacman_history(pacman_position_history, pacman_position)

        if self.min_distance == 0: self.score -= 200

        return self.score