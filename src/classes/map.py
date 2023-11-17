import pygame
from classes.animal.animal import Animal
from classes.planta.planta import Planta
from constants import *

class Map:
    def __init__(self,screen):
        self.screen = screen
        self.boardSurface = pygame.Surface((cellNum * cellSize, cellNum * cellSize))
        self.menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))
        self.organismos =[]
        self.initDisplay()
        self.initOrganism()
        self.drawOrganism()
        self.drawDisplay()

# Pantalla
    def initDisplay(self):
        self.drawBoard(self.boardSurface)
        self.menuSurface.fill(grey)

    def drawBoard(self,surface):
        for row in range (cellNum):
            for col in range (cellNum):
                if (row + col) % 2 == 0:
                    color = lighGreen
                else:
                    color = darkGreen
                pygame.draw.rect(surface, color, (col * cellSize, row * cellSize, cellSize, cellSize))

    def drawDisplay(self):
        self.screen.blit(self.menuSurface, (cellNum * cellSize, 0))
        self.screen.blit(self.boardSurface, (0, 0))
# Organismos
    def initOrganism(self):
        for i in range(10):
            animal = Animal(lionSprite)
            self.organismos.append(animal)
        for i in range (5):
            planta = Planta(plantaSprite)
            self.organismos.append(planta)
    def drawOrganism(self):
        for org in self.organismos:
            org.draw(self.boardSurface)
    def updateOrganism(self):
        for org in self.organismos:
            if isinstance(org, Animal):
                org.move()
        self.drawBoard(self.boardSurface)
        self.drawOrganism()