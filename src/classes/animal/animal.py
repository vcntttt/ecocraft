import random
from pygame.math import Vector2
from classes.organismo import Organismo
from constants import *
# tiene que cazar, descomponerse y morir
class Animal(Organismo):
    def __init__(self,sprite):
        super().__init__(sprite)
        self.genero = random.randint(0,1) #0 para hembra y 1 para macho
    def update(self):
        self.move()

    def move(self):
        dx = random.choice([-self.vel,0,self.vel])
        dy = random.choice([-self.vel,0,self.vel])
        
        newX = self.rect.x + dx * cellSize
        newY = self.rect.y + dy * cellSize

        newX = max(0, min(newX, (cellNum - 1) * cellSize))
        newY = max(0, min(newY, (cellNum - 1) * cellSize))

        self.rect.topleft = (newX, newY)

    def eat(self):
        self.energy += 10