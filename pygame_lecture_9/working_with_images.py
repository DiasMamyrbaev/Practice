import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Example")

# Load an image
image = pygame.image.load('your_image.png')  # Make sure the image is in the same directory

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with color
    screen.fill((255, 255, 255))

    # Draw the image on the screen
    screen.blit(image, (100, 100))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
