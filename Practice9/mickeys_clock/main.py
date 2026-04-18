import pygame
import sys
from clock import MickeyClock

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Clockmousemen")

    clock = MickeyClock(screen, WIDTH, HEIGHT)

    pygame_clock = pygame.time.Clock()

    last_update = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= 1000:
            clock.update()
            last_update = current_time

        screen.fill((255,255,255))
        clock.draw()
        pygame.display.flip()
        pygame_clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

