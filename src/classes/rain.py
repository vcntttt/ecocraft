import pygame
import random
from constants import *

class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((3, 15))
        self.image.fill(rainColor)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, visibleSize[0])
        self.rect.y = random.randint(-visibleSize[1], 0)
        self.speed = 40

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > visibleSize[1]:
            self.kill()