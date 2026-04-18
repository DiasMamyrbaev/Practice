import pygame
import sys

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music and Sound Example")

# Load background music
pygame.mixer.music.load('background_music.mp3')

# Play music (looping)
pygame.mixer.music.play(-1)  # -1 for infinite loop

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with color
    screen.fill((255, 255, 255))

    # Update display
    pygame.display.flip()

# Load a sound effect
sound = pygame.mixer.Sound('effect_sound.wav')

# Play the sound effect
sound.play()

# Quit Pygame
pygame.quit()
sys.exit()
