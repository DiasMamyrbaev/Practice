import pygame
import time
import math
import os
import random
from utils import scale_image, blit_rotate_center

pygame.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(filename):

    parent_dir = os.path.dirname(BASE_DIR) 
    return os.path.join(parent_dir, "Practice10", filename)

GRASS = scale_image(pygame.image.load(get_path("imgs/grass.jpg")), 2.5)
TRACK = scale_image(pygame.image.load(get_path("imgs/track.png")), 0.9)
TRACK_MASK = pygame.mask.from_surface(TRACK) # Добавляем маску асфальта

TRACK_BORDER = scale_image(pygame.image.load(get_path("imgs/track-border.png")), 0.9)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

FINISH = pygame.image.load(get_path("imgs/finish.png"))
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (130, 250)

RED_CAR = scale_image(pygame.image.load(get_path("imgs/red-car.png")), 0.55)


try:
    COIN_IMG = scale_image(pygame.image.load(get_path("imgs/coin.png")), 0.3)
except FileNotFoundError:

    COIN_IMG = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.circle(COIN_IMG, (255, 215, 0), (10, 10), 10)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 60
FONT = pygame.font.SysFont("comicsans", 30)
CRASH_FONT = pygame.font.SysFont("comicsans", 60, bold=True)

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        return mask.overlap(car_mask, offset)

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0

class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel * 0.4
        self.move()


class Coin:
    def __init__(self):
        self.img = COIN_IMG
        self.mask = pygame.mask.from_surface(self.img)
        self.x, self.y = self.get_valid_position()

    def get_valid_position(self):
        while True:
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            
            
            on_track = TRACK_MASK.overlap(self.mask, (x, y)) is not None
          
            off_border = TRACK_BORDER_MASK.overlap(self.mask, (x, y)) is None
            
            if on_track and off_border:
                return x, y

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

def draw(win, images, player_car, current_time, best_time, coins, score):
    for img, pos in images:
        win.blit(img, pos)


    for coin in coins:
        coin.draw(win)


    time_text = FONT.render(f"Time: {round(current_time, 2)}s", 1, (255, 255, 255))
    win.blit(time_text, (10, HEIGHT - 70))


    best_time_text = FONT.render(
        f"Best: {round(best_time, 2) if best_time != float('inf') else 0}s", 1, (255, 255, 255)
    )
    win.blit(best_time_text, (10, HEIGHT - 40))

    score_text = FONT.render(f"Coins: {score}", 1, (255, 215, 0))
    win.blit(score_text, (10, HEIGHT - 100))

    player_car.draw(win)
    pygame.display.update()

def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False
    if keys[pygame.K_a]: player_car.rotate(left=True)
    if keys[pygame.K_d]: player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()
    if not moved:
        player_car.reduce_speed()


run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
player_car = PlayerCar(6, 6)

start_time = time.time()
best_time = float('inf')


coins = []
score = 0
COIN_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_SPAWN_EVENT, 2000) 


coins.append(Coin())

while run:
    clock.tick(FPS)
    current_time = time.time() - start_time

    draw(WIN, images, player_car, current_time, best_time, coins, score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == COIN_SPAWN_EVENT:
            if len(coins) < 5:
                coins.append(Coin())

    move_player(player_car)


    for coin in coins[:]:
        if player_car.collide(coin.mask, coin.x, coin.y):
            coins.remove(coin)
            score += 1


    if player_car.collide(TRACK_BORDER_MASK) is not None:
        crash_text = CRASH_FONT.render("АВАРИЯ!", 1, (255, 0, 0))
        WIN.blit(crash_text, (WIDTH/2 - crash_text.get_width()/2, HEIGHT/2 - crash_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(1000)
        player_car.reset()
        start_time = time.time()
        score = 0
        coins.clear()
        coins.append(Coin()) 


    finish_poi_collide = player_car.collide(FINISH_MASK, *FINISH_POSITION)
    if finish_poi_collide is not None:
        if finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            if current_time < best_time:
                best_time = current_time
            
            print(f"Finish! Your time: {round(current_time, 2)}s | Coins collected: {score}")
            player_car.reset()
            start_time = time.time()
            score = 0
            coins.clear()
            coins.append(Coin())

pygame.quit()