import pygame
from bullet import Bullet
from alien import Alien

def check_events(settings, screen, spaceship, bullets):
    """Handle key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                spaceship.moving_right = True
            elif event.key == pygame.K_LEFT:
                spaceship.moving_left = True
            elif event.key == pygame.K_SPACE:
                fire_bullet(settings, screen, spaceship, bullets)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                spaceship.moving_right = False
            elif event.key == pygame.K_LEFT:
                spaceship.moving_left = False

def fire_bullet(settings, screen, spaceship, bullets):
    """Create a new bullet and add it to the bullets group."""
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, spaceship)
        bullets.add(new_bullet)

def update_bullets(bullets, aliens, screen, spaceship, scoreboard):
    """Update the position of bullets and check for collisions with aliens."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(bullets, aliens, screen, spaceship, scoreboard)

def check_bullet_alien_collisions(bullets, aliens, screen, spaceship, scoreboard):
    """Check for bullet-alien collisions and update the score."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            scoreboard.increase_score(len(aliens))

def update_aliens(aliens, spaceship, bullets, screen, scoreboard):
    """Update the position of the aliens and check for collisions with the spaceship."""
    aliens.update()

    if pygame.sprite.spritecollideany(spaceship, aliens):
        spaceship_hit(spaceship, bullets, aliens, scoreboard)

def spaceship_hit(spaceship, bullets, aliens, scoreboard):
    """Handle the event when the spaceship is hit by an alien."""
    if scoreboard.lives > 0:
        scoreboard.decrease_lives()
        aliens.empty()
        bullets.empty()

        # Reset the spaceship position
        spaceship.center_spaceship()
        create_fleet(settings, screen, aliens)

def create_fleet(settings, screen, aliens):
    """Create a full fleet of aliens."""
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, alien.rect.height)

    for row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row)

def get_number_aliens_x(settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = settings.screen_width - 2 * alien_width
    return available_space_x // (2 * alien_width)

def get_number_rows(settings, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = settings.screen_height - 3 * alien_height
    return available_space_y // (2 * alien_height)

def create_alien(settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the correct position."""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def update_screen(settings, screen, spaceship, bullets, aliens, scoreboard):
    """Update the screen and redraw everything."""
    screen.fill(settings.bg_color)

    # Redraw all bullets and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    spaceship.blitme()
    aliens.draw(screen)

    # Display the score
    scoreboard.show_score()

    # Make the most recently drawn screen visible
    pygame.display.flip()
