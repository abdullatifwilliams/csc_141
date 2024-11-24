import sys

pygame.init()

class Background:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Blue Background Window")
    
    def draw(self):
        self.surface.fill(self.color)

def main():
    window_width, window_height = 800, 600
    blue = (0, 222, 255)
    
    background = Background(blue, window_width, window_height)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        background.draw()
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
