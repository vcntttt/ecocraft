import pygame
from classes.ecosistema import Ecosistema
from classes.menu import Menu
from constants import *
class Map:
    def __init__(self,screen):
        self.screen = screen
        self.boardSurface = pygame.Surface((cellNum * cellSize, cellNum * cellSize))
        self.menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))
        self.ecosistema = Ecosistema()
        self.menu = Menu()
    def initDisplay(self):
        self.drawBoard(self.boardSurface)
        
    def drawBoard(self,surface):
        for row in range (cellNum):
            for col in range (cellNum):
                if (row + col) % 2 == 0:
                    color = lighGreen
                else:
                    color = darkGreen
                pygame.draw.rect(surface, color, (col * cellSize, row * cellSize, cellSize, cellSize))

    def drawDisplay(self):
        self.initDisplay()
        self.ecosistema.drawOrganism(self.boardSurface)
        self.screen.blit(self.boardSurface, (0, 0))
        self.menu.draw(self.screen, (cellNum * cellSize, 0))

    # Actualizar
    def updateHour(self, gameHour):
        self.menu.updateHour(gameHour)
    def updateStates(self):
        self.menu.updateStates(self.ecosistema.organismos)
    def updateOrganism(self):
        self.ecosistema.updateOrganism()