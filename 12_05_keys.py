import pygame
import sys

def main():
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Key Event Test")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                print(f"Key pressed: {event.key} ({pygame.key.name(event.key)})")

        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
