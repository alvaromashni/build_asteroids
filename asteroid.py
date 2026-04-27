import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        surface = screen
        color = "white"
        position = self.position
        radius = self.radius
        line_width = LINE_WIDTH
        pygame.draw.circle(surface, color, position, radius, line_width)

    def update(self, dt):
        velocity = self.velocity * dt
        self.position += velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        velocity1 *= 1.2
        velocity2 *= 1.2
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2