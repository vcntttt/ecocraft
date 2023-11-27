import random
from constants import *

class Organismo(pygame.sprite.Sprite):
    posiciones = set()
    def __init__(self, sprite, hp, nrg, nTrofico):
        super().__init__()
        # pygame sprites
        self.image = sprite
        self.rect = self.image.get_rect()
        # stats
        self.hp = hp
        self.maxHp = hp
        self.energy = nrg
        self.maxEnergy = nrg
        self.nivelTrofico = nTrofico
        # status
        self.isAlive = True
        self.isBorning = False
        self.borningTime = 25
        self.borningProgress = 0
        self.isDecomposing = False
        self.decompositionTime = 20
        self.decompositionProgress = 0

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
        self.isDecomposing = True

    def update(self,orgs):
        if self.isDecomposing:
            self.decompositionProgress += 1
            self.drawBar(yellow, self.decompositionProgress, self.decompositionTime)
            if self.decompositionProgress >= self.decompositionTime:
                from classes.animal.animal import Animal
                from classes.planta.planta import Planta
                if isinstance(self, Animal):
                    newPlant = Planta(plantaSprite)
                    newPlant.rect.topleft = self.rect.topleft
                    orgs.add(newPlant)
                self.kill()
                
        if self.isBorning:
            self.borningProgress += 1
            self.drawBar(red, self.borningProgress, self.borningTime)
            if self.borningProgress >= self.borningTime:
                self.isBorning = False
                self.isDecomposing = True
                self.decompositionProgress = 0
                self.hp = self.maxHp
                self.energy = self.maxEnergy

    def drawBar(self, color, param, total):
        barWidth = self.rect.width * (param / total)
        barHeight = 10
        bar = pygame.Surface((barWidth,barHeight))
        bar.fill(color)

        decomImg = self.image.copy()
        barPos = (0,self.rect.height - barHeight)
        decomImg.blit(bar,barPos)
        self.image = decomImg