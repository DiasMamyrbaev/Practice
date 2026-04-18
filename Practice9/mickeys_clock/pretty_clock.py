import pygame
import math
import datetime


pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Analog Clock')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


CLOCK_RADIUS = 250
CENTER = (WIDTH // 2, HEIGHT // 2)


font = pygame.font.SysFont(None, 40)

def draw_clock_face(screen):

    pygame.draw.circle(screen, WHITE, CENTER, CLOCK_RADIUS, 5)
    
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = CENTER[0] + (CLOCK_RADIUS - 40) * math.cos(angle)
        y = CENTER[1] + (CLOCK_RADIUS - 40) * math.sin(angle)
        
        text = font.render(str(i), True, WHITE)
        text_rect = text.get_rect(center=(int(x), int(y)))
        screen.blit(text, text_rect)

def draw_hand(screen, length, angle, color, width):
    end_x = CENTER[0] + length * math.cos(angle)
    end_y = CENTER[1] + length * math.sin(angle)
    pygame.draw.line(screen, color, CENTER, (end_x, end_y), width)

# Основной цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second

    hour_angle = math.radians((hours + minutes / 60) * 30 - 90)
    minute_angle = math.radians((minutes + seconds / 60) * 6 - 90)
    second_angle = math.radians(seconds * 6 - 90)

    window.fill(BLACK)
    draw_clock_face(window)

    draw_hand(window, CLOCK_RADIUS - 100, hour_angle, BLUE, 8)
    draw_hand(window, CLOCK_RADIUS - 60, minute_angle, GREEN, 6)
    draw_hand(window, CLOCK_RADIUS - 30, second_angle, RED, 2)

    pygame.draw.circle(window, WHITE, CENTER, 8)

    pygame.display.update()
    
    clock.tick(10)

pygame.quit()

