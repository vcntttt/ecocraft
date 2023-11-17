import random
from pygame.math import Vector2
from constants import *

class Organismo:
    posiciones = []
    def __init__(self, sprite):
        self.sprite = sprite
        self.hp = 100
        self.energy = 50
        self.vel = 1
        while True:
            self.x = random.randint(0, cellNum - 1)
            self.y = random.randint(0, cellNum - 1)
            self.pos = Vector2(self.x, self.y)
            if not (self.pos in self.posiciones):
                self.posiciones.append(self.pos)
                break

    def draw(self,boardSurface):
        boardSurface.blit(self.sprite, (self.pos.x * cellSize, self.pos.y * cellSize))