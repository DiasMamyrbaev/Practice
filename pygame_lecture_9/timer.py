import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Timer Example")

# Set up clock
clock = pygame.time.Clock()

# Start timer
start_time = pygame.time.get_ticks()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get elapsed time
    elapsed_time = pygame.time.get_ticks() - start_time
    print(f"Elapsed time: {elapsed_time / 1000:.2f} seconds")

    # Fill the screen with color
    screen.fill((255, 255, 255))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)  # 60 frames per second

# Quit Pygame
pygame.quit()
sys.exit()
