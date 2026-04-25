import pygame
import random
import sys
import os

pygame.init()

RES = 600
SIZE = 20
FPS = 5

screen = pygame.display.set_mode((RES, RES))
pygame.display.set_caption("Boozer Snake")
clock = pygame.time.Clock()


font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)

COLOR_GREEN = pygame.Color('green')
COLOR_RED = pygame.Color('red')
COLOR_ORANGE = pygame.Color('orange')
COLOR_BLACK = pygame.Color('black')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, '1.jpg')
bg_image = None
if os.path.exists(image_path):
    bg_image = pygame.image.load(image_path).convert()


snake_body = [(400, 400), (350, 400), (300, 400)]
dx, dy = SIZE, 0
score = 0
level = 1


direction_changed = False

def generate_food(snake):
    while True:
        x = random.randrange(0, RES - SIZE + 1, SIZE)
        y = random.randrange(0, RES - SIZE + 1, SIZE)
        if (x, y) not in snake:
            return x, y

food_x, food_y = generate_food(snake_body)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN and not direction_changed:
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and dy != SIZE:
                dx, dy = 0, -SIZE
                direction_changed = True
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and dy != -SIZE:
                dx, dy = 0, SIZE
                direction_changed = True
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and dx != SIZE:
                dx, dy = -SIZE, 0
                direction_changed = True
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and dx != -SIZE:
                dx, dy = SIZE, 0
                direction_changed = True


    head_x, head_y = snake_body[0]
    new_head = (head_x + dx, head_y + dy)
    
    direction_changed = False 


    if (new_head[0] < 0 or new_head[0] >= RES or 
        new_head[1] < 0 or new_head[1] >= RES or 
        new_head in snake_body):
        

        if bg_image:
            screen.blit(bg_image, (0, 0))
        else:
            screen.fill(COLOR_BLACK)
            
        render_end = font_end.render('GAME OVER', 1, COLOR_RED)
        end_rect = render_end.get_rect(center=(RES // 2, RES // 2))
        screen.blit(render_end, end_rect)
        
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()


    snake_body.insert(0, new_head)


    if new_head[0] == food_x and new_head[1] == food_y:
        score += 1
        food_x, food_y = generate_food(snake_body)
        if score % 3 == 0:
            level += 1
            FPS += 1 
    else:
        snake_body.pop()


    if bg_image:
        screen.blit(bg_image, (0, 0))
    else:
        screen.fill(COLOR_BLACK)
        
    pygame.draw.rect(screen, COLOR_RED, (food_x, food_y, SIZE, SIZE))
    
    for block in snake_body:
        pygame.draw.rect(screen, COLOR_GREEN, (block[0], block[1], SIZE - 1, SIZE - 1))

    render_score = font_score.render(f'SCORE: {score}   LEVEL: {level}', 1, COLOR_GREEN)
    screen.blit(render_score, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)