import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        image_path = os.path.join(current_dir, "images")
        
        bg_file = os.path.join(image_path, "mickeyclock.png") 
        self.bg_image = pygame.image.load(bg_file).convert()
        
        self.right_hand_img = pygame.image.load(os.path.join(image_path, "mickey_right_hand.png")).convert_alpha()
        self.left_hand_img = pygame.image.load(os.path.join(image_path, "mickey_left_hand.png")).convert_alpha()

        self.bg_image = pygame.transform.scale(self.bg_image, (self.width, self.height))
        self.bg_rect = self.bg_image.get_rect(center=self.center)

        self.minutes = 0
        self.seconds = 0

    def update(self):
        """Получаем текущее время системы"""
        now = datetime.datetime.now()
        self.minutes = now.minute
        self.seconds = now.second

    def blit_rotate_center(self, surf, image, center, angle):

        rotated_image = pygame.transform.rotate(image, angle)

        new_rect = rotated_image.get_rect(center=center)
 
        surf.blit(rotated_image, new_rect)

    def draw(self):
        self.screen.blit(self.bg_image, self.bg_rect)

        min_angle = -self.minutes * 6 + 90 
        
        sec_angle = -self.seconds * 6 + 90

        self.blit_rotate_center(self.screen, self.right_hand_img, self.center, min_angle)
        

        self.blit_rotate_center(self.screen, self.left_hand_img, self.center, sec_angle)

