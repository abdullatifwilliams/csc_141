import pygame
from settings import Settings
from spaceship import Spaceship
from alien import Alien
from bullet import Bullet
from game_functions import check_events, update_screen, update_bullets, update_aliens, create_fleet
from scoreboard import Scoreboard

def run_game():
    # Initialize pygame and settings
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a spaceship, a group of bullets, and a scoreboard
    spaceship = Spaceship(settings, screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    scoreboard = Scoreboard(settings, screen)

    # Create a fleet of aliens
    create_fleet(settings, screen, aliens)

    # Main game loop
    while True:
        check_events(settings, screen, spaceship, bullets)
        spaceship.update()
        update_bullets(bullets, aliens, screen, spaceship, scoreboard)
        update_aliens(aliens, spaceship, bullets, screen, scoreboard)
        update_screen(settings, screen, spaceship, bullets, aliens, scoreboard)

if __name__ == '__main__':
    run_game() 
