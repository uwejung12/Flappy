import pygame
import config

class Flappy():
    def __init__(self,screen):
        self.flappy = pygame.image.load("Images\Flappy.png")
        self.flappy.convert()
        self.rect = self.flappy.get_rect()
        self.rect.center = config.widht // 4, config.height // 2

    def draw(self, screen):
        screen.blit(self.flappy, self.rect)


    def move(self):
        self.rect.centery += 1