import pygame
import math
from Objetos import Objeto

class Projectile():
    def __init__(self,image, x, y, groups):
        self.projectile = []

        # self.image = pygame.image.load(image)
        # self.image = pygame.transform.scale(self.image, 
        #                             (self.image.get_width()/5, 
        #                                 self.image.get_height()/5))
    
        self.projectile_speed = 5
        self.projectile_radius = 5
        
        self.x = x
        self.y = y
    
    def shoot_projectile(self, px, py):
        projectile = {'x': px + 80, 'y': py + 72, 'angle': math.pi / 2}
        self.projectile.append(projectile)
        print(px, py)
        return
    
    def Get_Act_Firing(self, Window):
        for projectile in self.projectile :
            projectile['y'] -= int(self.projectile_speed * math.cos(projectile['angle']))
            projectile['x'] += int(self.projectile_speed * math.sin(projectile['angle']))
            pygame.draw.circle(Window, (205, 0, 205), (int(projectile['x']), int(projectile['y'])), self.projectile_radius)
            self.Projectile = [projectile for projectile in self.projectile  if 0 <= projectile['x'] <= 1280 and 0 <= projectile['y'] <= 720]
        return

    
    def update(self):
        return