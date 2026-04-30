import pygame
import time
import os
import random
from db import init_db, save_score_db, get_top_scores_db
from persistence import load_settings, save_score_json
from racer import PlayerCar, ChaserCar, Item, scale_image
import ui
from db import save_score_db
from persistence import save_score_json

pygame.init()


init_db()
settings = load_settings()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def get_asset(name): return os.path.join(BASE_DIR, "assets", name)

try:
    GRASS = scale_image(pygame.image.load(get_asset("grass.jpg")), 2.5)
    TRACK = scale_image(pygame.image.load(get_asset("track.png")), 0.9)
    TRACK_BORDER = scale_image(pygame.image.load(get_asset("track-border.png")), 0.9)
    FINISH = pygame.image.load(get_asset("finish.png"))
    RED_CAR = scale_image(pygame.image.load(get_asset("red-car.png")), 0.55)
    COIN_IMG = scale_image(pygame.image.load(get_asset("coin.png")), 0.3)
except Exception as e:
    print(f"Ошибка загрузки ассетов: {e}")
    pygame.quit()
    exit()

TRACK_MASK = pygame.mask.from_surface(TRACK)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POS = (130, 250)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer: TSIS 3")
FPS = 60


NITRO_IMG = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(NITRO_IMG, (0, 255, 255), (10, 10), 10)
SHIELD_IMG = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(SHIELD_IMG, (0, 255, 0), (10, 10), 10)

def main():
    run = True
    clock = pygame.time.Clock()
    state = "MENU"
    username = "Player1"
    
    player_car = PlayerCar(6, 6, RED_CAR)
    chaser_car = None
    coins = []
    powerups = []
    score = 0
    start_time = 0

    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 3000)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if state == "MENU" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_car.reset()
                    chaser_car = None
                    coins = [Item(COIN_IMG, TRACK_MASK, TRACK_BORDER_MASK, WIDTH, HEIGHT)]
                    powerups = []
                    score = 0
                    start_time = time.time()
                    state = "PLAYING"
                elif event.key == pygame.K_l:
                    state = "LEADERBOARD"

            elif state == "LEADERBOARD" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: state = "MENU"

            elif state == "GAME_OVER" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: state = "MENU"

            elif state == "PLAYING" and event.type == SPAWN_EVENT:
                if len(coins) < 5:
                    coins.append(Item(COIN_IMG, TRACK_MASK, TRACK_BORDER_MASK, WIDTH, HEIGHT))
                if len(powerups) < 2 and random.random() < 0.3:
                    ptype = random.choice(['nitro', 'shield'])
                    p_img = NITRO_IMG if ptype == 'nitro' else SHIELD_IMG
                    powerups.append({'type': ptype, 'obj': Item(p_img, TRACK_MASK, TRACK_BORDER_MASK, WIDTH, HEIGHT)})

  
        if state == "MENU":
            ui.draw_menu(WIN, WIDTH, HEIGHT)

        elif state == "LEADERBOARD":
            top_scores = get_top_scores_db(10)
            ui.draw_leaderboard(WIN, WIDTH, HEIGHT, top_scores)

        elif state == "GAME_OVER":
            ui.draw_game_over(WIN, WIDTH, HEIGHT)

        elif state == "PLAYING":
            current_time = time.time() - start_time


            if current_time > player_car.nitro_end_time:
                player_car.max_vel = player_car.base_max_vel
            if current_time >= 300 and chaser_car is None:
                chaser_img = RED_CAR.copy()
                chaser_img.fill((0, 0, 0, 100), special_flags=pygame.BLEND_RGBA_SUB)
                chaser_car = ChaserCar(5, 5, chaser_img, (WIDTH//2, HEIGHT//2))


            keys = pygame.key.get_pressed()
            moved = False
            if keys[pygame.K_a]: player_car.rotate(left=True)
            if keys[pygame.K_d]: player_car.rotate(right=True)
            if keys[pygame.K_w]: moved = True; player_car.move_forward()
            if keys[pygame.K_s]: moved = True; player_car.move_backward()
            if not moved: player_car.reduce_speed()

            if chaser_car:
                chaser_car.chase(player_car)
                if player_car.collide(pygame.mask.from_surface(chaser_car.img), chaser_car.x, chaser_car.y):
                    if player_car.shield:
                        player_car.shield = False
                        chaser_car = None
                    else:
                        state = "GAME_OVER"
                        save_score_db(username, score, current_time)
                        save_score_json(username, score, current_time)

  
            for coin in coins[:]:
                if player_car.collide(coin.mask, coin.x, coin.y):
                    coins.remove(coin); score += 1

            for pu in powerups[:]:
                if player_car.collide(pu['obj'].mask, pu['obj'].x, pu['obj'].y):
                    if pu['type'] == 'nitro':
                        player_car.max_vel = player_car.base_max_vel + 3
                        player_car.nitro_end_time = current_time + 4
                    elif pu['type'] == 'shield': player_car.shield = True
                    powerups.remove(pu)

            if player_car.collide(TRACK_BORDER_MASK) is not None:
                if player_car.shield:
                    player_car.shield = False; player_car.bounce()
                else:
                    state = "GAME_OVER"
                    save_score_db(username, score, current_time)
                    save_score_json(username, score, current_time)

 
            finish_collision = player_car.collide(FINISH_MASK, *FINISH_POS)
            if finish_collision is not None:
                if finish_collision[1] == 0: 
                    player_car.bounce()
                else:
                    state = "GAME_OVER"
                    save_score_db(username, score, current_time)
                    save_score_json(username, score, current_time)


            WIN.blit(GRASS, (0, 0))
            WIN.blit(TRACK, (0, 0))
            WIN.blit(FINISH, FINISH_POS)
            WIN.blit(TRACK_BORDER, (0, 0))
            for coin in coins: coin.draw(WIN)
            for pu in powerups: pu['obj'].draw(WIN)
            player_car.draw(WIN)
            if chaser_car: chaser_car.draw(WIN)
            ui.draw_hud(WIN, current_time, score, username, player_car.shield, HEIGHT)
            
            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()


