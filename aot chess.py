import pygame
import os
#print("Current working directory:", os.getcwd())

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("attack on titan chess")

# Function to draw the chessboard
def draw_chessboard():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(screen, BLUE, 
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


soldier = pygame.image.load('soldier.png')
soldier = pygame.transform.scale(soldier, (SQUARE_SIZE, SQUARE_SIZE))
def draw_pieces():
    for row in range(ROWS):
        for col in range(2):
            screen.blit(soldier, (SQUARE_SIZE * row, SQUARE_SIZE * col))
    for row in range(ROWS):
        for col in range(6, 8):
            screen.blit(soldier, (SQUARE_SIZE * row, SQUARE_SIZE * col))  

def get_square_from_mouse(pos, square_size):
    """Calculate which chessboard square was clicked."""
    x, y = pos
    row = y // square_size
    col = x // square_size
    return row, col

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_chessboard()
    draw_pieces()
    pygame.display.flip()
# Quit Pygame
pygame.quit()