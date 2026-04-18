import pygame
import os
import glob

class MusicPlayer:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.playlist = []
        self.load_tracks()
        
        if not self.playlist:
            self.create_demo_tracks()
        
        self.current_track_index = 0
        self.current_position = 0
        self.is_playing = False
        self.is_paused = False
        self.volume = 0.7 
        
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.volume)
        

        self.title_font = pygame.font.Font(None, 48)
        self.info_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.colors = {
            'background': (30, 30, 40),
            'text': (255, 255, 255),
            'highlight': (100, 200, 255),
            'progress_bg': (60, 60, 70),
            'progress_fg': (100, 200, 255),
            'button': (80, 80, 100),
            'button_hover': (120, 120, 140)
        }
        
        self.track_length = 0
        self.update_timer = 0
        
    def load_tracks(self):
        music_folder = "music"
        
        formats = ['*.mp3', '*.wav', '*.ogg']
        
        if os.path.exists(music_folder):
            for format in formats:
                tracks = glob.glob(os.path.join(music_folder, format))
                self.playlist.extend(tracks)
            
            self.playlist.sort()
            
            if self.playlist:
                print(f"Загружено треков: {len(self.playlist)}")
                for i, track in enumerate(self.playlist):
                    print(f"{i+1}. {os.path.basename(track)}")
        else:
            print(f"Папка '{music_folder}' не найдена")
    
    def create_demo_tracks(self):
        """Создание демо-треков, если нет реальных файлов"""
        print("Создаем демо-треки...")
        
        if not os.path.exists("music"):
            os.makedirs("music")
            print("Папка 'music' создана")
        
        demo_tracks = [
            "Track 1 - Introduction",
            "Track 2 - Main Theme", 
            "Track 3 - Interlude",
            "Track 4 - Finale"
        ]
        
        for i, track_name in enumerate(demo_tracks, 1):
            track_file = f"music/demo_track_{i}.txt"
            with open(track_file, 'w') as f:
                f.write(f"Demo track: {track_name}\n")
                f.write("Please add real MP3/WAV files to the music folder\n")
            
            self.playlist.append(track_file)
        
        print(f"Создано {len(demo_tracks)} демо-треков")
    
    def play_music(self):
        if not self.playlist:
            print("Нет треков в плейлисте")
            return
        
        track_path = self.playlist[self.current_track_index]
        
        if track_path.endswith(('.mp3', '.wav', '.ogg')):
            try:
                if self.is_paused:
                    pygame.mixer.music.unpause()
                    self.is_paused = False
                else:
                    pygame.mixer.music.load(track_path)
                    pygame.mixer.music.play()
                    self.get_track_length()
                
                self.is_playing = True
                print(f"Воспроизведение: {os.path.basename(track_path)}")
                
            except pygame.error as e:
                print(f"Ошибка воспроизведения: {e}")
                self.is_playing = False
        else:
            print(f"Демо-трек: {os.path.basename(track_path)}")
            self.is_playing = True
            self.track_length = 180
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.current_position = 0
        print("Воспроизведение остановлено")
    
    def pause_resume(self):
        if self.is_playing:
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
                print("Воспроизведение возобновлено")
            else:
                pygame.mixer.music.pause()
                self.is_paused = True
                print("Пауза")
    
    def next_track(self):
        if self.playlist:
            self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
            self.stop_music()
            self.play_music()
            print(f"Следующий трек: {self.get_current_track_name()}")
    
    def previous_track(self):
        if self.playlist:
            self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
            self.stop_music()
            self.play_music()
            print(f"Предыдущий трек: {self.get_current_track_name()}")
    
    def restart_track(self):
        if self.is_playing:
            self.stop_music()
            self.play_music()
            print("Трек перезапущен")
    
    def volume_up(self):
        self.volume = min(1.0, self.volume + 0.1)
        pygame.mixer.music.set_volume(self.volume)
        print(f"Громкость: {int(self.volume * 100)}%")
    
    def volume_down(self):
        self.volume = max(0.0, self.volume - 0.1)
        pygame.mixer.music.set_volume(self.volume)
        print(f"Громкость: {int(self.volume * 100)}%")
    
    def get_current_track_name(self):
        """Получение имени текущего трека"""
        if self.playlist:
            return os.path.basename(self.playlist[self.current_track_index])
        return "No tracks"
    
    def get_track_length(self):
        """Получение длительности трека"""
        self.track_length = 240
        
        try:
            import mutagen
            from mutagen.mp3 import MP3
            from mutagen.wave import WAVE
            
            track_path = self.playlist[self.current_track_index]
            if track_path.endswith('.mp3'):
                audio = MP3(track_path)
                self.track_length = audio.info.length
            elif track_path.endswith('.wav'):
                audio = WAVE(track_path)
                self.track_length = audio.info.length
        except ImportError:
            pass
        except:
            pass
    
    def get_current_position(self):

        if self.is_playing and not self.is_paused:
            try:
                pos = pygame.mixer.music.get_pos()
                if pos != -1:
                    self.current_position = pos / 1000
            except:
                pass
            

        if self.is_playing and self.track_length > 0:
            if self.current_position >= self.track_length - 0.5: 
                self.next_track()
    
        return min(self.current_position, self.track_length)
    
    def draw_progress_bar(self):
        """Отрисовка полосы прогресса"""
        bar_x = 100
        bar_y = self.screen_height - 100
        bar_width = self.screen_width - 200
        bar_height = 20
        

        pygame.draw.rect(self.screen, self.colors['progress_bg'],
                        (bar_x, bar_y, bar_width, bar_height))
        
        if self.track_length > 0:
            progress = self.get_current_position() / self.track_length
            filled_width = int(bar_width * min(progress, 1.0))
            pygame.draw.rect(self.screen, self.colors['progress_fg'],
                            (bar_x, bar_y, filled_width, bar_height))
        

        current_time = self.format_time(self.get_current_position())
        total_time = self.format_time(self.track_length)
        
        time_text = self.small_font.render(f"{current_time} / {total_time}", 
                                           True, self.colors['text'])
        self.screen.blit(time_text, (bar_x + bar_width//2 - 50, bar_y - 25))
    
    def format_time(self, seconds):
        """Форматирование времени из секунд"""
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes:02d}:{secs:02d}"
    
    def draw_playlist(self):
        """Отрисовка плейлиста"""
        playlist_y = 150
        start_x = 50
        
        title = self.info_font.render("Playlist:", True, self.colors['highlight'])
        self.screen.blit(title, (start_x, playlist_y - 30))
        

        for i, track in enumerate(self.playlist[:8]):
            track_name = os.path.basename(track).replace('.txt', '').replace('_', ' ')
            if len(track_name) > 40:
                track_name = track_name[:37] + "..."
            
            if i == self.current_track_index:
                color = self.colors['highlight']
                prefix = "▶ "
            else:
                color = self.colors['text']
                prefix = f"{i+1}. "
            
            track_text = self.small_font.render(f"{prefix}{track_name}", 
                                                True, color)
            self.screen.blit(track_text, (start_x, playlist_y + i * 25))
    
    def draw_controls_info(self):
        """Отрисовка информации об управлении"""
        controls = [
            "Controls:",
            "P - Play | S - Stop | Space - Pause/Resume",
            "N - Next Track | B - Previous Track | R - Restart",
            "↑ - Volume Up | ↓ - Volume Down | Q - Quit"
        ]
        
        start_y = self.screen_height - 180
        for i, control in enumerate(controls):
            if i == 0:
                color = self.colors['highlight']
                font = self.info_font
            else:
                color = self.colors['text']
                font = self.small_font
            
            text = font.render(control, True, color)
            self.screen.blit(text, (50, start_y + i * 25))
    
    def draw_status(self):
        """Отрисовка плеера"""

        if self.is_playing:
            if self.is_paused:
                status = "⏸ Paused"
                color = (255, 255, 100)
            else:
                status = "▶ Playing"
                color = (100, 255, 100)
        else:
            status = "⏹ Stopped"
            color = (255, 100, 100)
        
        status_text = self.title_font.render(status, True, color)
        self.screen.blit(status_text, (self.screen_width//2 - 80, 50))
        
        track_name = self.get_current_track_name()
        if len(track_name) > 50:
            track_name = track_name[:47] + "..."
        
        track_text = self.info_font.render(f"Current Track: {track_name}", 
                                          True, self.colors['highlight'])
        track_rect = track_text.get_rect(center=(self.screen_width//2, 110))
        self.screen.blit(track_text, track_rect)
        
        volume_text = self.small_font.render(f"Volume: {int(self.volume * 100)}%", 
                                            True, self.colors['text'])
        self.screen.blit(volume_text, (self.screen_width - 150, 20))
    
    def draw(self):
        """Основной метод отрисовки"""
   
        self.screen.fill(self.colors['background'])
        
        self.draw_status()
        self.draw_progress_bar()
        self.draw_playlist()
        self.draw_controls_info()
        
        pygame.draw.rect(self.screen, self.colors['button'], (10, 10, self.screen_width - 20, self.screen_height - 20), 2)


