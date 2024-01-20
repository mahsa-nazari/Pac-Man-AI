import pygame
from settings import *
from gameboard import GameBoard
from characters import Pacman, Ghost
from ai import GameAI  # Import the AI class
import random 
from collections import deque


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pacman Game")


pacman_initial_position = (10, 7)
ghosts_initial_positions = [(11, 5), (8, 5)]
loss = 0

board = GameBoard(window, pacman_initial_position, ghosts_initial_positions)


pacman = Pacman(10, 7)
ghosts = [Ghost(11, 5, RED), Ghost(8, 5, PINK)]



# Now, pass this instance when creating the GameAI object
game_ai = GameAI(max_depth=16, v=False)

running = True
clock = pygame.time.Clock()

is_pacman_turn = True
step = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)

    # Update Pac-Man's position using the Minimax algorithm
    if is_pacman_turn:
        _, pacman_next_move = game_ai.minimax(board, 6, float('-inf'), float('inf'), True)  # True for Pacman
        #board.update_pacman_position(pacman_next_move)
        board.apply_move(pacman_next_move, is_pacman=True, ghost_index=None)

    else:
        # Update Ghosts' positions randomly
        new_ghosts_positions = []
        for i in range(2):
            ghost_moves = board.get_possible_moves(False, i)  # False for ghosts, i is the index
            if ghost_moves:
                new_pos = random.choice(ghost_moves)  # Choose a move randomly
                new_ghosts_positions.append(new_pos)

        board.update_ghosts_positions(new_ghosts_positions)

    board.draw()
    step +=1
    print('step',step)
    game_ai.log()
    if game_ai.dot == 99:
        print('You won!')
        running = False
    if board.is_game_over():
        print("Game Over!")
        running = False

    pygame.display.flip()
    is_pacman_turn = not is_pacman_turn

    # Slow down the game a bit more
    clock.tick(200)

pygame.quit()