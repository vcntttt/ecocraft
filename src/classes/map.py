import pygame
from classes.menu import Menu
from classes.ecosistema import Ecosistema
from constants import *
class Map:
    def __init__(self,screen):
        self.screen = screen
        self.boardSurface = pygame.Surface((cellNum * cellSize, cellNum * cellSize))
        self.menu = Menu(self.screen)
        self.ecosistema = Ecosistema()
        self.initDisplay()
        self.drawDisplay()

# Pantalla
    def initDisplay(self):
        self.drawBoard(self.boardSurface)
        self.menu.fillMenu()

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
        self.menu.draw()
        self.screen.blit(self.boardSurface, (0, 0))
        
    def updateOrganism(self):
        self.ecosistema.updateOrganism()