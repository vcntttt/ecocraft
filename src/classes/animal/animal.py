import random
from classes.organismo import Organismo
from constants import *
# tiene que cazar, descomponerse y morir
class Animal(Organismo):
    def __init__(self,sprite):
        super().__init__(sprite)
        self.tipo = 0 #0 para los herbivoros y 1 para los carnivoros
    def move(self):
        dx = random.choice([-self.vel,0,self.vel])
        dy = random.choice([-self.vel,0,self.vel])

        newX = max(0,min(cellNum - 1, self.pos.x + dx))
        newY = max(0,min(cellNum - 1, self.pos.y + dy))

        self.pos.x=newX
        self.pos.y=newY