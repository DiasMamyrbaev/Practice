import pygame
import sys
from ball import Ball



pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Moving Ball")
baller = Ball(x=400, y=300, radius=25, color=(255,0,0), screen_width=WIDTH, screen_height=HEIGHT)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                baller.move(0,-20)
            elif event.key == pygame.K_RIGHT:
                baller.move(20,0)
            elif event.key == pygame.K_DOWN:
                baller.move(0,20)
            elif event.key == pygame.K_LEFT:
                baller.move(-20,0)

    screen.fill((255,255,255))

    clock.tick(60)

    baller.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
