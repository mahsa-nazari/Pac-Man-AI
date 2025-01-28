import pygame
from settings import *
from gameboard import GameBoard
from characters import Pacman, Ghost
from ai import GameAI  # Import the AI class
import random 
from collections import deque
from moviepy import VideoClip 

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pacman Game")


pacman_initial_position = (10, 7)
ghosts_initial_positions = [(11, 5), (8, 5)]
loss = 0

board = GameBoard(window, pacman_initial_position, ghosts_initial_positions)


pacman = Pacman(10, 7)
ghosts = [Ghost(11, 5, RED), Ghost(8, 5, PINK)]


game_ai = GameAI(v=False)

running = True
clock = pygame.time.Clock()
frames = []
is_pacman_turn = True
step = 0
last_dot_eaten_step = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)

    # Update Pac-Man's position using the Minimax algorithm
    if is_pacman_turn:
        # Tracking the number of dots eaten and steps since the last dot was eaten
        dots = board.dot
        steps_since_last_dot = step - last_dot_eaten_step

        # Default depth for the Minimax algorithm
        depth = 4
        step +=1

        # Adjusting the depth based on how long it's been since Pac-Man last ate a dot
        if steps_since_last_dot >= 50:
            depth = 6

        # Using the Minimax algorithm to decide Pac-Man's next move with the current depth
        _, pacman_next_move = game_ai.minimax(board, depth, float('-inf'), float('inf'), True)  # True for Pacman
        
        # Applying the chosen move to Pac-Man
        board.apply_move(pacman_next_move, is_pacman=True, ghost_index=None)
        # Update the last dot eaten step if Pac-Man eats a dot in this move
        if board.dot > dots: last_dot_eaten_step = step

        # game_ai.log()

    else:
        # Update Ghosts' positions randomly
        new_ghosts_positions = []
        for i in range(2):
            ghost_moves = board.get_possible_moves(False, i)  # False for ghosts, i is the index
            if ghost_moves:
                new_pos = random.choice(ghost_moves)  # Choose a move randomly
                new_ghosts_positions.append(new_pos)

        # Update the positions of the ghosts on the board
        board.update_ghosts_positions(new_ghosts_positions)

    board.draw()

    frame = pygame.surfarray.array3d(window)  
    frames.append(frame.transpose([1, 0, 2])) 

    if game_ai.dot == 99:
        running = False
    if board.is_game_over():
        running = False

    pygame.display.flip()
    is_pacman_turn = not is_pacman_turn


    clock.tick(100)

pygame.quit()

if frames:
    print("Saving video...")
    clip = VideoClip(lambda t: frames[int(t * 200)], duration=len(frames) / 200)  # 200 FPS
    clip.write_videofile("pacman_gameplay.mp4", fps=200)
    print("Video saved as pacman_gameplay.mp4")