import random
from constants import *

class Organismo(pygame.sprite.Sprite):
    posiciones = set()

    def __init__(self, sprite):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        # old
        self.hp = 100
        self.energy = 50
        self.vel = 1
        while True:
            newPos = (random.randint(0, cellNum - 1)*cellSize, random.randint(0, cellNum - 1)*cellSize)
            if newPos not in self.posiciones:
                self.posiciones.add(newPos)
                break
        self.rect.topleft = newPos