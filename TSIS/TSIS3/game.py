import pygame
import random
import sys

RES = 600
SIZE = 20
BASE_FPS = 5

# Цвета
COLOR_GREEN = pygame.Color('green')
COLOR_RED = pygame.Color('red')
COLOR_DARKRED = pygame.Color(139, 0, 0)
COLOR_BLACK = pygame.Color('black')
COLOR_GOLD = pygame.Color('gold')
COLOR_WHITE = pygame.Color('white')
COLOR_BLUE = pygame.Color('blue')
COLOR_CYAN = pygame.Color('cyan')
COLOR_GREY = pygame.Color('grey')

def get_random_pos(exclude_lists):
    while True:
        x = random.randrange(0, RES - SIZE + 1, SIZE)
        y = random.randrange(0, RES - SIZE + 1, SIZE)
        pos = (x, y)
        collision = False
        for lst in exclude_lists:
            if pos in lst:
                collision = True
                break
        if not collision:
            return pos

def run_game(screen, clock, settings, personal_best):
    """
    Основной игровой цикл. 
    Возвращает (score, level) при проигрыше.
    """
    font_score = pygame.font.SysFont('Arial', 26, bold=True)
    
    snake_body = [(400, 400), (350, 400), (300, 400)]
    dx, dy = SIZE, 0
    score = 0
    level = 1
    FPS = BASE_FPS
    obstacles = []
    
    food_pos = get_random_pos([snake_body])
    food_weight = random.choices([1, 3], weights=[80, 20])[0]
    food_spawn_time = pygame.time.get_ticks()
    
    poison_pos = get_random_pos([snake_body, [food_pos]])
    
    powerup_pos = (-SIZE, -SIZE)
    powerup_type = None
    powerup_spawn_time = 0
    active_powerup = None
    powerup_start_time = 0
    shield_active = False
    
    while True:
        current_time = pygame.time.get_ticks()
        screen.fill(COLOR_BLACK)
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and dy != SIZE:
                    dx, dy = 0, -SIZE
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and dy != -SIZE:
                    dx, dy = 0, SIZE
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and dx != SIZE:
                    dx, dy = -SIZE, 0
                elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and dx != -SIZE:
                    dx, dy = SIZE, 0

        # Таймер еды
        if current_time - food_spawn_time > 6000:
            food_pos = get_random_pos([snake_body, obstacles, [poison_pos]])
            food_weight = random.choices([1, 3], weights=[80, 20])[0]
            food_spawn_time = current_time
            
        # Спавн Power-up
        if powerup_pos == (-SIZE, -SIZE) and random.randint(1, 100) == 1:
            powerup_pos = get_random_pos([snake_body, obstacles, [food_pos], [poison_pos]])
            powerup_type = random.choice(['SPEED', 'SLOW', 'SHIELD'])
            powerup_spawn_time = current_time
            
        # Исчезновение Power-up
        if powerup_pos != (-SIZE, -SIZE) and current_time - powerup_spawn_time > 8000:
            powerup_pos = (-SIZE, -SIZE)
            
        # Окончание эффекта Power-up
        if active_powerup in ['SPEED', 'SLOW'] and current_time - powerup_start_time > 5000:
            FPS = BASE_FPS + (level * 2)
            active_powerup = None

        # Движение
        head_x, head_y = snake_body[0]
        new_head = (head_x + dx, head_y + dy)

        # Столкновения
        is_collision = (new_head[0] < 0 or new_head[0] >= RES or 
                        new_head[1] < 0 or new_head[1] >= RES or 
                        new_head in snake_body or 
                        new_head in obstacles)
                        
        if is_collision:
            if shield_active:
                shield_active = False
                dx, dy = -dx, -dy
                new_head = (head_x + dx, head_y + dy)
            else:
                return score, level # КОНЕЦ ИГРЫ

        snake_body.insert(0, new_head)

        # Съедание обычной еды
        if new_head == food_pos:
            score += food_weight
            food_pos = get_random_pos([snake_body, obstacles, [poison_pos]])
            food_weight = random.choices([1, 3], weights=[80, 20])[0]
            food_spawn_time = current_time
            
            new_level = 1 + score // 5
            if new_level > level:
                level = new_level
                FPS = BASE_FPS + (level * 2)
                if level >= 3:
                    for _ in range(level * 2):
                        ob_pos = get_random_pos([snake_body, [food_pos], [poison_pos]])
                        obstacles.append(ob_pos)
        else:
            snake_body.pop()
            
        # Съедание яда
        if new_head == poison_pos:
            snake_body = snake_body[:-2]
            poison_pos = get_random_pos([snake_body, obstacles, [food_pos]])
            if len(snake_body) <= 1:
                return score, level # КОНЕЦ ИГРЫ
                
        # Съедание Power-up
        if new_head == powerup_pos:
            if powerup_type == 'SPEED':
                FPS += 10
                active_powerup = 'SPEED'
            elif powerup_type == 'SLOW':
                FPS = max(3, FPS - 5)
                active_powerup = 'SLOW'
            elif powerup_type == 'SHIELD':
                shield_active = True
                
            powerup_start_time = current_time
            powerup_pos = (-SIZE, -SIZE)

        # Отрисовка
        if settings.get("grid"):
            for x in range(0, RES, SIZE):
                pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, RES))
            for y in range(0, RES, SIZE):
                pygame.draw.line(screen, (40, 40, 40), (0, y), (RES, y))

        f_color = COLOR_GOLD if food_weight > 1 else COLOR_RED
        pygame.draw.rect(screen, f_color, (food_pos[0], food_pos[1], SIZE, SIZE))
        pygame.draw.rect(screen, COLOR_DARKRED, (poison_pos[0], poison_pos[1], SIZE, SIZE))
        
        if powerup_pos != (-SIZE, -SIZE):
            pygame.draw.rect(screen, COLOR_BLUE, (powerup_pos[0], powerup_pos[1], SIZE, SIZE))
            
        for ob in obstacles:
            pygame.draw.rect(screen, COLOR_GREY, (ob[0], ob[1], SIZE, SIZE))

        s_color = tuple(settings.get("snake_color", [0, 255, 0]))
        if shield_active:
            s_color = COLOR_CYAN
            
        for block in snake_body:
            pygame.draw.rect(screen, s_color, (block[0], block[1], SIZE - 1, SIZE - 1))

        txt = font_score.render(f'SCORE: {score}  LVL: {level}  BEST: {personal_best}', 1, COLOR_WHITE)
        screen.blit(txt, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)
    
