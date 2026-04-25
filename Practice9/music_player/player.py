import pygame
import os
import glob

class MusicPlayer:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        pygame.mixer.init()

        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.is_paused = False
        self.volume = 0.7
        self.track_length = 0.0

        pygame.mixer.music.set_volume(self.volume)

        self.font_big   = pygame.font.Font(None, 52)
        self.font_med   = pygame.font.Font(None, 34)
        self.font_small = pygame.font.Font(None, 26)

        self.WHITE   = (255, 255, 255)
        self.CYAN    = (80, 200, 240)
        self.GREEN   = (80, 220, 100)
        self.YELLOW  = (255, 220, 60)
        self.RED     = (240, 80, 80)
        self.GRAY    = (160, 160, 170)
        self.DARK    = (45, 45, 58)
        self.BAR_BG  = (70, 70, 85)

        self._load_playlist()



    def _load_playlist(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        music_dir = os.path.join(base_dir, "music")
        if not os.path.exists(music_dir):
            print(f"Папка '{music_dir}' не найдена")
            return

        for ext in ("*.mp3", "*.wav", "*.ogg", "*.MP3", "*.WAV", "*.OGG"):
            self.playlist.extend(glob.glob(os.path.join(music_dir, ext)))
            self.playlist.extend(glob.glob(os.path.join(music_dir, "**", ext), recursive=True))

        # убираем дубли
        seen = set()
        unique = []
        for p in self.playlist:
            key = os.path.normcase(p)
            if key not in seen:
                seen.add(key)
                unique.append(p)
        self.playlist = sorted(unique)

        print(f"Найдено треков: {len(self.playlist)}")
        for i, t in enumerate(self.playlist):
            print(f"  {i+1}. {os.path.basename(t)}")

    def _track_name(self, index=None):
        if not self.playlist:
            return "нет треков :("
        if index is None:
            index = self.current_index
        name = os.path.basename(self.playlist[index])
        
        #убираем расширение
        name = os.path.splitext(name)[0]
        return name

    def play_music(self):
        if not self.playlist:
            return

        path = self.playlist[self.current_index]

        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            self.is_playing = True
            self.is_paused  = False
            self.track_length = self._get_length(path)
            print(f"{self._track_name()}")
        except pygame.error as e:
            print(f"Ошибка pygame: {e}")
            self.is_playing = False

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused  = False
        print("Остановлено")

    def pause_resume(self):
        if not self.is_playing:
            return
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            print("Возобновлено")
        else:
            pygame.mixer.music.pause()
            self.is_paused = True
            print("Пауза")

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_music()

    def previous_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play_music()

    def restart_track(self):
        if self.is_playing:
            self.play_music()

    def volume_up(self):
        self.volume = min(1.0, round(self.volume + 0.1, 1))
        pygame.mixer.music.set_volume(self.volume)
        print(f"Громкость: {int(self.volume * 100)}%")

    def volume_down(self):
        self.volume = max(0.0, round(self.volume - 0.1, 1))
        pygame.mixer.music.set_volume(self.volume)
        print(f"Громкость: {int(self.volume * 100)}%")


    def _get_length(self, path):
        try:
            ext = os.path.splitext(path)[1].lower()
            if ext == ".mp3":
                from mutagen.mp3 import MP3
                return MP3(path).info.length
            elif ext == ".wav":
                from mutagen.wave import WAVE
                return WAVE(path).info.length
            elif ext == ".ogg":
                from mutagen.oggvorbis import OggVorbis
                return OggVorbis(path).info.length
        except Exception as e:
            print(f"mutagen: не удалось получить длину — {e}")
        return 0.0

    def _current_pos(self):
        if not self.is_playing:
            return 0.0
        ms = pygame.mixer.music.get_pos()
        return ms / 1000.0 if ms >= 0 else 0.0

    def _fmt(self, secs):
        secs = max(0, int(secs))
        return f"{secs // 60:02d}:{secs % 60:02d}"

  
    def draw(self):
        W, H = self.screen_width, self.screen_height


        if self.is_playing:
            status_txt = "Пауза" if self.is_paused else "Играет"
            status_col = self.YELLOW if self.is_paused else self.GREEN
        else:
            status_txt = "Остановлено"
            status_col = self.RED

        surf = self.font_big.render(status_txt, True, status_col)
        self.screen.blit(surf, surf.get_rect(centerx=W // 2, y=30))


        name = self._track_name()
        if len(name) > 48:
            name = name[:45] + "…"
        surf = self.font_med.render(name, True, self.CYAN)
        self.screen.blit(surf, surf.get_rect(centerx=W // 2, y=95))

        #громкость
        vol_surf = self.font_small.render(f"Громкость: {int(self.volume * 100)}%",
                                          True, self.GRAY)
        self.screen.blit(vol_surf, (W - 180, 18))

        #прогресс
        self._draw_progress(W, H)

        # плейлис
        self._draw_playlist(W)

        #подсказки
        self._draw_hints(H)

        # рамка
        pygame.draw.rect(self.screen, self.DARK, (8, 8, W - 16, H - 16), 2)

    def _draw_progress(self, W, H):
        bx, by  = 80, H - 95
        bw, bh  = W - 160, 18

        pygame.draw.rect(self.screen, self.BAR_BG, (bx, by, bw, bh), border_radius=9)

        pos = self._current_pos()
        if self.track_length > 0:
            ratio = min(pos / self.track_length, 1.0)
            fill  = int(bw * ratio)
            if fill > 0:
                pygame.draw.rect(self.screen, self.CYAN,
                                 (bx, by, fill, bh), border_radius=9)

        time_str = f"{self._fmt(pos)} / {self._fmt(self.track_length)}"
        t = self.font_small.render(time_str, True, self.WHITE)
        self.screen.blit(t, t.get_rect(centerx=W // 2, y=by - 22))

    def _draw_playlist(self, W):
        x, y = 50, 145
        header = self.font_med.render("Плейлист:", True, self.CYAN)
        self.screen.blit(header, (x, y))
        y += 35

        visible = self.playlist[:9]
        for i, path in enumerate(visible):
            name = os.path.splitext(os.path.basename(path))[0]
            if len(name) > 46:
                name = name[:43] + "…"

            if i == self.current_index:
                col  = self.CYAN
                line = f"{name}"
            else:
                col  = self.WHITE
                line = f"{i + 1}.  {name}"

            surf = self.font_small.render(line, True, col)
            self.screen.blit(surf, (x, y + i * 26))

    def _draw_hints(self, H):
        lines = [
            ("Управление:", self.CYAN, self.font_med),
            ("P — Play    S — Stop    Space — Пауза/Продолжить", self.WHITE, self.font_small),
            ("N — Следующий    B — Предыдущий    R — Рестарт", self.WHITE, self.font_small),
            ("UP — Громче    DOWN — Тише    Q — Выход", self.WHITE, self.font_small),
        ]
        y = H - 250
        for text, col, font in lines:
            self.screen.blit(font.render(text, True, col), (50, y))
            y += 28


