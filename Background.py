import pygame
from Objetos import Objeto

class Background(Objeto):
    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (1280, 720))
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y