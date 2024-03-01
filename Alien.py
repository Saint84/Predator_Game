import pygame
from Objetos import Objeto
from random import randint
from Animation import Animation_Enemy_Walk

class Alien(Objeto):
    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_width()/3, 
                                             self.image.get_height()/3))
        

        # self.rect = self.image.get_rect(center=(800, randint(200, 550)))
        self.rect[0] = x
        self.rect[1] = y

        self.Player_Speed = 2
        self.Current_Frame = 0
        self.Frame_Counter = 0
        self.Frame_Delay = 10
    
    def draw(self, Animation):
        self.Frame_Counter += 1
        if self.Frame_Counter >= self.Frame_Delay:
            self.Frame_Counter = 0
            self.Current_Frame = (self.Current_Frame + 1 ) % (len(Animation))
            
            self.image = pygame.transform.scale(Animation[self.Current_Frame],
                                                (Animation[self.Current_Frame].get_width()/3,
                                                Animation[self.Current_Frame].get_height()/3))
            
            self.image = pygame.transform.flip(self.image, True, False)
        return
    
    def update(self):
        self.rect.x -= 2
        if self.rect.x == 50:
            print('d')
            self.kill()
        self.draw(Animation_Enemy_Walk)