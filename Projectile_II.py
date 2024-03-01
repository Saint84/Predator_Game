import pygame
from Objetos import Objeto

class Projectile_II(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Assets/Projectile_1.png',)
        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_width()/5, 
                                             self.image.get_height()/5))
        
        self.rect = self.image.get_rect(center=(x , y))
    
    def update(self):
        self.rect.x += 10
        return