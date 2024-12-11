import pygame

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the spaceship image and set its rect
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the spaceship at the center bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the spaceship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the spaceship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_spaceship(self):
        """Center the spaceship on the screen."""
        self.center = self.screen_rect.centerx
        self.rect.centerx = self.center
