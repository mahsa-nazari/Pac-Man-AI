class GameStateEvaluator:
    def __init__(self):
        self.loss = 0

    def evaluate_state(self, game_board, v=True):
        """
        Evaluate the current state of the game board and return a loss.
        A higher loss typically means a more favorable state for Pac-Man.
        """
        # Example scoring logic: Pac-Man should avoid ghosts
        distances = (game_board.pacman_ghost_distance(0), game_board.pacman_ghost_distance(1))
        self.min_distance = min(distances)
        loss_multiplier = 10  # Adjust this multiplier as needed
        #import dot eatign score from board
        self.dot = game_board.dot
        m = 1
        #if self.min_distance == 0: self.loss = -20
        #elif self.min_distance == 1: self.loss = -10
        #elif self.min_distance == 2: self.loss = -5
        if self.dot > 30: m = 50
        elif self.dot >50: m =100
        elif self.dot >90: m =200
        self.loss = m * self.dot
        #self.loss = self.dot_score -  # +1 to avoid division by zero
        if v: print("loss", self.loss, "minimun distance", self.min_distance, "dots_eaten: ", self.dot)
        return self.loss





        """""
        self.ghostloss = loss_multiplier / (self.min_distance + 1)  # +1 to avoid division by zero
        #import dot eatign score from board
        self.dot_score = game_board.score
        
    
        # Efficiency - Add penalty for uneaten dots, encourages faster completion
        uneaten_dots = 99 - (self.dot_score/10)
        efficiency_loss = 5 * uneaten_dots  # Adjust multiplier as needed

        #return 1/self.loss + 1.7 * self.dot_score

        self.loss = 1/self.ghostloss + (1.5 * self.dot_score) 
        return 1/self.ghostloss + 1.7 * self.dot_score - uneaten_dots
        """

    
    
    