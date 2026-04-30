import pygame

pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 30)
TITLE_FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MENU_FONT = pygame.font.SysFont("comicsans", 40)

def draw_menu(win, width, height):
    win.fill((50, 50, 50))
    title = TITLE_FONT.render("RACING GAME", 1, (255, 255, 255))
    play_btn = MENU_FONT.render("[ SPACE ] Play", 1, (0, 255, 0))
    lb_btn = MENU_FONT.render("[ L ] Leaderboard", 1, (255, 255, 0))
    set_btn = MENU_FONT.render("[ S ] Settings", 1, (0, 255, 255))
    
    win.blit(title, (width//2 - title.get_width()//2, 100))
    win.blit(play_btn, (width//2 - play_btn.get_width()//2, 250))
    win.blit(lb_btn, (width//2 - lb_btn.get_width()//2, 330))
    win.blit(set_btn, (width//2 - set_btn.get_width()//2, 410))
    pygame.display.update()

def draw_hud(win, current_time, score, username, has_shield, height):
    time_text = FONT.render(f"Time: {round(current_time, 2)}s", 1, (255, 255, 255))
    score_text = FONT.render(f"Coins: {score}", 1, (255, 215, 0))
    user_text = FONT.render(f"Player: {username}", 1, (200, 200, 200))
    
    win.blit(time_text, (10, height - 70))
    win.blit(score_text, (10, height - 40))
    win.blit(user_text, (10, 10))

    if has_shield:
        shield_txt = FONT.render("SHIELD ACTIVE", 1, (0, 255, 0))
        win.blit(shield_txt, (10, 40))

def draw_game_over(win, width, height):
    crash_text = TITLE_FONT.render("GAME OVER", 1, (255, 0, 0))
    hint_text = MENU_FONT.render("Press ESC for Menu", 1, (255, 255, 255))
    win.blit(crash_text, (width//2 - crash_text.get_width()//2, height//2 - 50))
    win.blit(hint_text, (width//2 - hint_text.get_width()//2, height//2 + 50))
    pygame.display.update()

def draw_leaderboard(win, width, height, top_scores):
    win.fill((30, 30, 50))
    title = TITLE_FONT.render("TOP SCORES (DB)", 1, (255, 255, 255))
    win.blit(title, (width//2 - title.get_width()//2, 50))
    
    y = 150
    for idx, row in enumerate(top_scores):
        txt = FONT.render(f"{idx+1}. {row[0]} - Coins: {row[1]} - Time: {round(row[2],1)}s", 1, (200, 200, 200))
        win.blit(txt, (100, y))
        y += 40
        
    back = MENU_FONT.render("Press ESC to Back", 1, (255, 100, 100))
    win.blit(back, (width//2 - back.get_width()//2, height - 80))
    pygame.display.update()