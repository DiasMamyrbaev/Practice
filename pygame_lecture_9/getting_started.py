import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Example")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with color
    screen.fill((255, 255, 255))  # RGB (white)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
