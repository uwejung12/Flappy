import pygame
import config
import Flappy

class Game:
    def __init__(self, mode):
        self.mode = mode
        self.FPS = 100

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode([config.widht, config.height])

        flappy = Flappy.Flappy(screen)

        spielaktiv = True

        x = 250
        y = 250

        while spielaktiv:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    spielaktiv = False

            screen.fill((255, 255, 255))

            flappy.draw(screen)

            flappy.move()

            pygame.display.flip()
            clock.tick(self.FPS)

        pygame.quit()