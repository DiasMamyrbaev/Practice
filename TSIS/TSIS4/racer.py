import pygame
import math
import random
import os

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)

class AbstractCar:
    def __init__(self, max_vel, rotation_vel, image, start_pos):
        self.img = image
        self.max_vel = max_vel
        self.base_max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = start_pos
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left: self.angle += self.rotation_vel
        elif right: self.angle -= self.rotation_vel

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
        self.y -= math.cos(radians) * self.vel
        self.x -= math.sin(radians) * self.vel

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        return mask.overlap(car_mask, offset)

class PlayerCar(AbstractCar):
    def __init__(self, max_vel, rotation_vel, image, start_pos=(180, 200)):
        super().__init__(max_vel, rotation_vel, image, start_pos)
        self.shield = False
        self.nitro_end_time = 0
        self.START_POS = start_pos

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel * 0.4
        self.move()

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0
        self.shield = False
        self.max_vel = self.base_max_vel

class ChaserCar(AbstractCar):
    def chase(self, player):
        dx, dy = player.x - self.x, player.y - self.y
        self.angle = math.degrees(math.atan2(-dy, dx)) - 90
        self.move_forward()

class Item:
    def __init__(self, img_surface, track_mask, border_mask, width, height):
        self.img = img_surface
        self.mask = pygame.mask.from_surface(self.img)
        self.x, self.y = self.get_valid_position(track_mask, border_mask, width, height)

    def get_valid_position(self, track_mask, border_mask, w, h):
        while True:
            x, y = random.randint(50, w - 50), random.randint(50, h - 50)
            if track_mask.overlap(self.mask, (x, y)) and not border_mask.overlap(self.mask, (x, y)):
                return x, y

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))