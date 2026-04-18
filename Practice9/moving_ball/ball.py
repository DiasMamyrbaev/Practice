import pygame
import sys

class Ball:
    def __init__(self, x, y, radius, color, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.sw = screen_width
        self.sh = screen_height

    def move(self, dx, dy):
        if self.radius <= self.x + dx <= self.sw - self.radius:
            self.x += dx
        if self.radius <= self.y + dy <= self.sh - self.radius:
            self.y += dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

