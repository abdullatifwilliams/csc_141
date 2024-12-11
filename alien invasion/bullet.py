import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, screen, spaceship):
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set its correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top

        # Store the bullet's position as a float for smoother movement.
        self.y = float(self.rect.y)

        # Set the bullet's speed
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
