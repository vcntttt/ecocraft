import random
from constants import *

class Organismo(pygame.sprite.Sprite):
    posiciones = set()
    def __init__(self, sprite, hp, nrg, nTrofico):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.hp = hp
        self.maxHp = hp
        self.energy = nrg
        self.maxEnergy = nrg
        self.nivelTrofico = nTrofico
        self.isAlive = True

        while True:
            newPos = (random.randint(0, cellNum - 1)*cellSize, random.randint(0, cellNum - 1)*cellSize)
            if newPos not in self.posiciones:
                self.posiciones.add(newPos)
                break
        self.rect.topleft = newPos

        def die(self):
            greyImg = pygame.Surface(self.image.get_size())
            greyImg = greyImg.convert_alpha()
            for x in range(greyImg.get_width()):
                for y in range(self.image.get_height()):
                    red,green,blue,alpha = self.image.get_at((x,y))
                    grey = (red + green + blue) // 3
                    greyImg.set_at((x,y),(grey,grey,grey,alpha))
            self.image = greyImg
            self.isAlive = False