import pygame
from circleshape import *
from constants import LINE_WIDTH

line_width = LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, line_width)

    def update(self, dt):
        self.position += self.velocity * dt
