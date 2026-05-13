import pygame
import random
from circleshape import *
from constants import *
from logger import log_event

line_width = LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, line_width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        pos_split = self.velocity.rotate(split_angle)
        neg_split = self.velocity.rotate(split_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroids = (
            Asteroid(self.position.x, self.position.y, new_radius),
            Asteroid(self.position.x, self.position.y, new_radius)
        )

        ast1, ast2 = new_asteroids
        ast1.velocity = pos_split * 1.2
        ast2.velocity = neg_split * 1.2
