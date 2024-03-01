import pygame
from Projectile_II import Projectile_II
from Animation import Animation_Walk, Animation_Fire, Animation_Idle

class Predator(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image = pygame.image.load('Assets/predatormask_idle_0.png')
        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_width()/3, 
                                             self.image.get_height()/3))
        
        self.rect = self.image.get_rect()
        self.Projectile = group[0]

        self.Player_Speed = 2
        self.Current_Frame = 0
        self.Frame_Counter = 0
        self.Frame_Delay = 10

        self.Moving = False
        self.Moving_Right = False
        self.Moving_Left = False
        self.Moving_Up = False
        self.Moving_Down = False


    def Get_Animation_Walking(self, Animation):
        self.Frame_Counter += 1
        if self.Frame_Counter >= self.Frame_Delay:
            self.Frame_Counter = 0
            self.Current_Frame = (self.Current_Frame + 1 ) % (len(Animation))
            
            self.image = pygame.transform.scale(Animation[self.Current_Frame],
                                                (Animation[self.Current_Frame].get_width()/3,
                                                Animation[self.Current_Frame].get_height()/3))
            
            if self.Moving_Left is True and self.Moving_Right is False:
                self.image = pygame.transform.flip(self.image, True, False)

    def Get_Animation_Fire(self, Animation):
        self.Frame_Counter += 3
        if self.Frame_Counter >= self.Frame_Delay:
            self.Frame_Counter = 0
            self.Current_Frame = (self.Current_Frame + 1 ) % (len(Animation))
            
            self.image = pygame.transform.scale(Animation[self.Current_Frame],
                                                (Animation[self.Current_Frame].get_width()/3,
                                                Animation[self.Current_Frame].get_height()/3))
        return

    def Get_Fire(self):
        if len(self.Projectile) < 15:
            self.Projectile.add(
                Projectile_II(*self.rect.center))
        return

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.Moving_Right = True
            if self.rect[0] < (1250 - 40):
                self.rect[0] += self.Player_Speed
                self.Get_Animation_Walking(Animation_Walk)

        elif keys[pygame.K_a]:
            self.Moving_Right = False
            self.Moving_Left = True
            if self.rect[0] > 0:
                self.rect[0] -= self.Player_Speed
                self.Get_Animation_Walking((Animation_Walk))

        elif keys[pygame.K_w]:
            self.Moving_Up = True
            self.Moving_Down= False
            if self.rect[1] > 150:
                self.rect[1] -= self.Player_Speed
                self.Get_Animation_Walking((Animation_Walk))

        elif keys[pygame.K_s]:
            self.Moving_Up = False
            self.Moving_Down= True
            if self.rect[1] < 500:
                self.rect[1] += self.Player_Speed
                self.Get_Animation_Walking((Animation_Walk))
        
        elif keys[pygame.K_SPACE]:
            self.Get_Animation_Fire(Animation_Fire)
    
        else:
            self.Get_Animation_Walking(Animation_Idle)

        return
