import pygame 
from random import randint, uniform

class Gota():
    def __init__(self):
        self.x = randint(0,500)
        self.y = randint(-200, -20)
        self.yspeed = uniform(0.5, 1)
        self.tamano = randint(10, 20)

    def caida(self):
        self.y += self.yspeed
        self.yspeed += 0.005

        if self.y > 300:
            self.y = randint(-200, -20)
            self.yspeed = uniform(0.5, 1)
        
    def show(self, screen):
        pygame.draw.line(screen, (0, 191, 255), (self.x, self.y), (self.x, self.y + self.tamano), 2)
