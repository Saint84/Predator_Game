import pygame
from Game import Game
from Alien import Alien
from random import randint

class Main():
    def __init__(self) -> None:
        self.Display = pygame.display.set_caption('Predator vs Alien')
        self.Surface = pygame.display.set_mode((1250, 720))

        self.Running = True
        self.Round = 1
        self.Score = 0
        self.Game = Game()
        return
    
    def update(self):
        while self.Running:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.Running = False
                if events.type == pygame.KEYUP:
                    if events.key == pygame.K_SPACE:
                        self.Game.Predator.Get_Fire()
                if self.Round % 5 == 0:
                    self.Game.Alien_Sprite.add(Alien('Assets/blue_idle_1.png', 1000, randint(50, 500), self.Game.Alien_Sprite))

            self.Game.draw(self.Surface)
            self.Game.update()
            
            pygame.time.Clock().tick(120)
            pygame.display.update()

            if pygame.sprite.groupcollide(self.Game.Projectile_Sprite, self.Game.Alien_Sprite, True, True):
                self.Score += 1
            
            self.Round += 1

            


if __name__ == '__main__':
    Main().update()
