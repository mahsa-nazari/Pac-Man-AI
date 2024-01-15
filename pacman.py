import pygame
from settings import *
from gameboard import GameBoard
from characters import Pacman, Ghost

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pacman Game")

board = GameBoard(window)
<<<<<<< HEAD
pacman = Pacman(5, 4)
ghosts = [Ghost(1, 1, RED), Ghost(16, 7, PINK)]
=======
pacman = Pacman(10, 7)
ghosts = [Ghost(10, 5, RED), Ghost(9, 5, PINK)]
>>>>>>> 19ea877 (Initial commit)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)
    board.draw()
    pacman.draw(window)
    for ghost in ghosts:
        ghost.draw(window)

    pygame.display.update()

pygame.quit()