import pygame
from Background import Background
from Player import Predator
from Alien import Alien
from random import randint

class Game:
    def __init__(self):
        # Background.
        self.Background_Sprite = pygame.sprite.GroupSingle()
        self.Background = Background('Assets/background_0.png', 0, 0, self.Background_Sprite)

        #Projectile
        self.Projectile_Sprite = pygame.sprite.Group()

        #Player
        self.Predator_Sprite = pygame.sprite.Group()
        self.Predator = Predator(self.Projectile_Sprite)

        #Enemy
        self.Alien_Sprite = pygame.sprite.Group()
        self.Alien = Alien('Assets/blue_idle_1.png', 1000, randint(50, 500), self.Alien_Sprite)

        #Game
        self.Score = 0
        return

    def draw(self, WINDOW):
        self.Background_Sprite.draw(WINDOW)
        self.Projectile_Sprite.draw(WINDOW)
        self.Predator_Sprite.draw(WINDOW)
        self.Alien_Sprite.draw(WINDOW)
        return

    def update(self):
        self.Background_Sprite.update()
        self.Projectile_Sprite.update()
        self.Predator_Sprite.update()
        self.Alien_Sprite .update()
        return