import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

radius = PLAYER_RADIUS
line_width = LINE_WIDTH
turn_speed = PLAYER_TURN_SPEED
speed = PLAYER_SPEED
shoot_speed = PLAYER_SHOOT_SPEED
shot_cd = PLAYER_SHOOT_COOLDOWN_SECONDS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white", self.triangle(), line_width)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shot_timer = max(0, self.shot_timer - dt)

    def rotate(self, dt):
        self.rotation += turn_speed * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * speed * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * shoot_speed
        self.shot_timer = shot_cd



