import pygame
from constants import *

class Sol(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sunSprite
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.visible = False
        self.resetPosition()

    def resetPosition(self):
        self.rect.x = 0
        self.rect.y = 0
        self.visible = False

    def update(self,gameHour):
        if minHrSol <= gameHour <=maxHrSol:
            if not self.visible:
                self.visible = True
                self.rect.x = 0 -self.image.get_width()
        timeInterval = maxHrSol - minHrSol
        self.speed = visibleSize[0] / (timeInterval * 60)  
        self.rect.x += self.speed
        if self.rect.x > visibleSize[0]:
            self.resetPosition()
        else: 
            self.visible = False
            
    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect.topleft)