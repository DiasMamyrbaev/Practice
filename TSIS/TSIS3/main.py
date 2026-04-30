import pygame
import sys
import os
import json
import db
import game

pygame.init()
db.init_db()

RES = 600
screen = pygame.display.set_mode((RES, RES))
pygame.display.set_caption("Boozer Snake: Advanced")
clock = pygame.time.Clock()

font_large = pygame.font.SysFont('Arial', 66, bold=True)
font_medium = pygame.font.SysFont('Arial', 36, bold=True)
font_small = pygame.font.SysFont('Arial', 24, bold=True)

COLOR_WHITE = pygame.Color('white')
COLOR_GREEN = pygame.Color('green')
COLOR_GOLD = pygame.Color('gold')
COLOR_RED = pygame.Color('red')
COLOR_BLACK = pygame.Color('black')
COLOR_GREY = pygame.Color('grey')

SETTINGS_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    return {"snake_color": [0, 255, 0], "grid": False, "sound": True}

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)

def draw_text(text, font, color, center_pos):
    render = font.render(text, True, color)
    rect = render.get_rect(center=center_pos)
    screen.blit(render, rect)

def main():
    settings = load_settings()
    state = "MENU"
    username = ""
    last_score, last_level = 0, 0
    top_10 = []

    while True:
        screen.fill(COLOR_BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if state == "MENU":
                    if event.key == pygame.K_RETURN and len(username) > 0:
                        state = "PLAYING"
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif event.key == pygame.K_l:
                        top_10 = db.get_top_10()
                        state = "LEADERBOARD"
                    elif event.key == pygame.K_s:
                        state = "SETTINGS"
                    elif event.unicode.isalnum() and len(username) < 15:
                        username += event.unicode
                        
                elif state == "GAME_OVER":
                    if event.key == pygame.K_r:
                        state = "PLAYING"
                    elif event.key == pygame.K_m:
                        state = "MENU"
                        
                elif state == "LEADERBOARD" or state == "SETTINGS":
                    if event.key == pygame.K_b:
                        state = "MENU"
                
                # Примитивное управление настройками (кнопка G включает/выключает сетку)
                if state == "SETTINGS" and event.key == pygame.K_g:
                    settings["grid"] = not settings["grid"]
                    save_settings(settings)

        # Рендеринг экранов
        if state == "MENU":
            draw_text("BOOZER SNAKE", font_large, COLOR_GREEN, (RES//2, 100))
            draw_text("Username: " + username + "_", font_medium, COLOR_GOLD, (RES//2, 250))
            draw_text("ENTER - Play", font_small, COLOR_WHITE, (RES//2, 350))
            draw_text("L - Leaderboard", font_small, COLOR_WHITE, (RES//2, 400))
            draw_text("S - Settings", font_small, COLOR_WHITE, (RES//2, 450))

        elif state == "PLAYING":
            # Вызываем саму игру из game.py
            personal_best = db.get_personal_best(username)
            last_score, last_level = game.run_game(screen, clock, settings, personal_best)
            
            # Игра закончилась
            db.save_result(username, last_score, last_level)
            state = "GAME_OVER"

        elif state == "GAME_OVER":
            draw_text("GAME OVER", font_large, COLOR_RED, (RES//2, 200))
            draw_text(f"Score: {last_score} | Level: {last_level}", font_medium, COLOR_WHITE, (RES//2, 300))
            draw_text("R - Retry  |  M - Menu", font_small, COLOR_GREY, (RES//2, 450))

        elif state == "LEADERBOARD":
            draw_text("TOP 10 PLAYERS", font_large, COLOR_GOLD, (RES//2, 80))
            y_offset = 180
            for i, record in enumerate(top_10):
                # record: (username, score, level_reached, date)
                text = f"{i+1}. {record[0]} - {record[1]} pts (Lvl {record[2]})"
                draw_text(text, font_small, COLOR_WHITE, (RES//2, y_offset))
                y_offset += 35
            draw_text("B - Back to Menu", font_small, COLOR_GREY, (RES//2, 550))
            
        elif state == "SETTINGS":
            draw_text("SETTINGS", font_large, COLOR_WHITE, (RES//2, 150))
            grid_status = "ON" if settings["grid"] else "OFF"
            draw_text(f"Press 'G' to toggle Grid: {grid_status}", font_medium, COLOR_GREEN, (RES//2, 300))
            draw_text("B - Save & Back", font_small, COLOR_GREY, (RES//2, 500))

        pygame.display.flip()
        clock.tick(15)

if __name__ == "__main__":
    main()

