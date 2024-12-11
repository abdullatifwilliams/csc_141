import pygame.font

class Scoreboard:
    """Class to report scoring information."""
    
    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # Font settings for displaying score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Initialize score and lives
        self.score = 0
        self.high_score = 0
        self.lives = 3

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_lives()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = "Score: " + str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score_str = "High Score: " + str(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Display the high score at the top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_lives(self):
        """Turn the number of remaining lives into a rendered image."""
        lives_str = "Lives: " + str(self.lives)
        self.lives_image = self.font.render(lives_str, True, self.text_color)

        # Display the lives at the top left of the screen
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = 20
        self.lives_rect.top = 20

    def show_score(self):
        """Draw the score and high score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lives_image, self.lives_rect)

    def increase_score(self, points):
        """Increase the score by the given points."""
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score
        self.prep_score()
        self.prep_high_score()

    def decrease_lives(self):
        """Decrease the number of lives."""
        self.lives -= 1
        if self.lives <= 0:
            self.reset_game()

    def reset_game(self):
        """Reset the game state after losing all lives."""
        self.lives = 3
        self.score = 0
        self.prep_score()
        self.prep_lives()
