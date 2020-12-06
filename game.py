import pygame
import config
import Flappy

class Game:
    def __init__(self):
        self.FPS = 100

    def reset(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([config.widht, config.height])
        self.flappy = Flappy.Flappy(self.screen)
        self.timer = 0
        self.done = False
        self.reward = 0

    def step(self, space):
        # while spielaktiv:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Spieler hat Leertaste gedrückt")
                    self.flappy.up()

        if space == 1:
            self.flappy.up()

        self.screen.fill((255, 255, 255))

        self.flappy.draw(self.screen)

        self.flappy.move()

        pygame.display.flip()

        self.clock.tick(self.FPS)

        if self.timer == 99:
            self.done = True
            pygame.quit()
        else:
            self.timer += 1

        self.reward += 1

        return self.reward, self.done

    # pygame.quit()
