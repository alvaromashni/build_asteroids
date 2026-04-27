import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

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