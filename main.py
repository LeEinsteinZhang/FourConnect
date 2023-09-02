import pygame
from pygame.locals import *
from logic import *

# Initialize pygame
pygame.init()

# Define colors
WHITE = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (50, 50, 50)

# Define dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600 + 50  # Extra 50 pixels for displaying the current player
CELL_SIZE = 100

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Connect 4')


def draw_current_player(player):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Current Player: {"RED" if player == 1 else "YELLOW"}', True, WHITE)
    screen.blit(text, (20, 10))


def draw_board(board):
    for row in range(Connect.HEIGHT):
        for col in range(Connect.WIDTH):
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE + 50, CELL_SIZE, CELL_SIZE))  # Black border
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE + 5, row * CELL_SIZE + 5 + 50, CELL_SIZE - 10, CELL_SIZE - 10))  # White background
            pygame.draw.circle(screen, WHITE,
                               (int(col * CELL_SIZE + CELL_SIZE / 2), int(row * CELL_SIZE + CELL_SIZE / 2 + 50)), 40)

            char = board.get_char(col, row)
            if char == 1:
                pygame.draw.circle(screen, RED,
                                   (int(col * CELL_SIZE + CELL_SIZE / 2), int(row * CELL_SIZE + CELL_SIZE / 2 + 50)), 40)
            elif char == 2:
                pygame.draw.circle(screen, YELLOW,
                                   (int(col * CELL_SIZE + CELL_SIZE / 2), int(row * CELL_SIZE + CELL_SIZE / 2 + 50)), 40)


game = Connect()
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            col = event.pos[0] // CELL_SIZE
            game.connect_drop_piece(col)
            if game.connect_has_finished():
                if game.connect_has_won() == 0:
                    print("The game ended with a draw.")
                else:
                    print(f"Player {game.connect_has_won()} wins!")
                game = Connect()

    draw_board(game)
    draw_current_player(game.current_player)
    pygame.display.flip()

pygame.quit()

