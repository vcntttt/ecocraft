import pygame
from classes.ecosistema import Ecosistema
from classes.menu import Menu
from constants import *

import pygame
from classes.ecosistema import Ecosistema
from classes.menu import Menu
from constants import *

class Map:
    def __init__(self,screen):
        # Principal
        self.screen = screen
        self.boardSurface = pygame.Surface((cellNum * cellSize, cellNum * cellSize))
        self.ecosistema = Ecosistema()
        self.menu = Menu()
        self.matrix = map
    def initDisplay(self):
        self.drawBoard(self.boardSurface)

    def drawBoard(self,surface):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                cell = self.matrix[row][col]
                if cell == 1:
                    sprite = p1Sprite
                #elif cell == 2:
                surface.blit(sprite,(col * cellSize, row * cellSize))

    def drawDisplay(self):
        self.initDisplay()
        self.ecosistema.orgsGroup.draw(self.boardSurface)
        self.screen.blit(self.boardSurface, (0, 0))
        self.menu.draw(self.screen, (cellNum * cellSize, 0))

    def update(self,gameHour):
        self.menu.updateHour(gameHour)
        self.menu.updateStates(self.ecosistema.orgsGroup)
        self.ecosistema.update()
        self.ecosistema.orgsGroup.update(self.ecosistema.orgsGroup)