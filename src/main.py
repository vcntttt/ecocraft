import pygame, sys

from classes.animal import Animal
from classes.planta import Planta
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ecocraft')
        self.screen = pygame.display.set_mode((cellNum * cellSize + menuWidth, cellNum * cellSize))
        self.clock = pygame.time.Clock()
        self.map = Map(self.screen)
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.map.drawDisplay()

            pygame.display.update()
            self.clock.tick(60)

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
    def drawDisplay(self):
        self.screen.blit(self.menuSurface, (cellNum * cellSize, 0))
        self.screen.blit(self.boardSurface, (0, 0))

game = Game()
game.run()