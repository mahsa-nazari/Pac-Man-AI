import pygame
from settings import *
from gameboard import GameBoard
from characters import Pacman, Ghost
from ai import GameAI  # Import the AI class
from game_state_evaluator import GameStateEvaluator
import random 
from pygame import time


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pacman Game")


pacman_initial_position = (10, 7)
ghosts_initial_positions = [(11, 5), (8, 5)]

board = GameBoard(window, pacman_initial_position, ghosts_initial_positions)


pacman = Pacman(10, 7)
ghosts = [Ghost(11, 5, RED), Ghost(8, 5, PINK)]



state_evaluator = GameStateEvaluator()

# Now, pass this instance when creating the GameAI object
game_ai = GameAI(max_depth=3, state_evaluator=state_evaluator)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)

    # Update Pac-Man's position using the Minimax algorithm
    _, pacman_next_move = game_ai.minimax(board, 3, float('-inf'), float('inf'), True)  # True for Pacman
    print('-------------------------------------------------------------')
    if pacman_next_move:
        board.update_pacman_position(pacman_next_move)

    # Update Ghosts' positions randomly
    new_ghost_positions = []
    for i in range(2):
        ghost_moves = board.get_possible_moves(False, i)  # False for ghosts, i is the index
        print('ghost_moves', ghost_moves)
        print('-------------------------------------------------------------', ghost_moves)
        if ghost_moves:
            new_pos = random.choice(ghost_moves)  # Choose a move randomly
            new_ghost_positions.append(new_pos)
    print("new_ghost_positions", new_ghost_positions)
    board.update_ghosts_positions(new_ghost_positions)

    board.draw()

    if board.is_game_over():
        print("Game Over!")
        running = False

    pygame.display.flip()
    clock.tick(10)

pygame.quit()