import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Geometric Shapes Example")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with color
    screen.fill((255, 255, 255))

    # Draw a rectangle (x, y, width, height)
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))

    # Draw a circle (x, y, radius)
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 50)

    # Draw a line (start_pos, end_pos, color, width)
    pygame.draw.line(screen, (0, 255, 0), (100, 100), (400, 400), 5)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
