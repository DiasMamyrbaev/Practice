import pygame
import sys
from player import MusicPlayer

def main():
    pygame.init()
    pygame.mixer.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player - Keyboard Controls")

    player = MusicPlayer(screen, WIDTH, HEIGHT)

    clock = pygame.time.Clock()

    print("Управление")
    print("P - Play | S - Stop | Space - Пауза")
    print("N - Следующий | B - Предыдущий | R - Рестарт")
    print("UP - Громче | DOWN - Тише | Q - Выход")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                print(f"[DEBUG] key={event.key} name='{pygame.key.name(event.key)}' scancode={event.scancode}")

                if event.key == pygame.K_p:
                    player.play_music()
                elif event.key == pygame.K_s:
                    player.stop_music()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.previous_track()
                elif event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE:
                    player.pause_resume()
                elif event.key == pygame.K_r:
                    player.restart_track()
                elif event.key == pygame.K_UP:
                    player.volume_up()
                elif event.key == pygame.K_DOWN:
                    player.volume_down()

        screen.fill((30, 30, 40))
        player.draw()
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
