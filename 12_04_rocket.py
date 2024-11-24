import sys
import pygame

class AlienInvasion:
    # Overall class to manage game assets and behavior

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")

        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 200, 255)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        
        #Ship Settings
        self.ship_image = pygame.image.load('22raptor.png')
        original_width, original_height = self.ship_image.get_rect().size
        new_width = original_width // 3
        new_height = original_height // 3
        self.ship_image = pygame.transform.scale(self.ship_image, (new_width, new_height))
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.midbottom = self.screen.get_rect().midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def run_game(self):
        while True:
            self._check_events()
            self.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_UP:
                    self.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_UP:
                    self.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.moving_down = False

    def update(self):

        if self.moving_right and self.ship_rect.right < self.screen_width:
            self.ship_rect.x += 1
        if self.moving_left and self.ship_rect.left > 0:
            self.ship_rect.x -= 1
        if self.moving_up and self.ship_rect.top > 0:
            self.ship_rect.y -= 1
        if self.moving_down and self.ship_rect.bottom < self.screen_height:
            self.ship_rect.y += 1

    
    
    def _update_screen(self):
        #redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        self.screen.blit(self.ship_image, self.ship_rect)
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    pygame.quit()
