import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the alien image and set its rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get
