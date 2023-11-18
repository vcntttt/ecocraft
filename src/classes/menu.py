import pygame
from constants import *

class Menu:
    def __init__(self,screen):
        self.menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))
        self.screen = screen
        self.fillMenu()

    def fillMenu(self):
        self.menuSurface.fill(grey)

    def updateHour(self,gameHour):
        self.fillMenu()
        h1Font = pygame.font.SysFont('Comic Sans MS', 30)
        text = h1Font.render('Hour: ' + str(gameHour), True, black)
        self.menuSurface.blit(text, (10, 10))
        
    def draw (self):
        self.screen.blit(self.menuSurface, (cellNum * cellSize, 0))
    # def updateStates(self,organismos):
    #     normalFont = pygame.font.SysFont('Comic Sans MS', 12)
    #     ypos = 650
    #     for organismo in organismos:
    #         text = normalFont.render(str(organismo.__class__.__name__) , True, black)
    #         self.menuSurface.blit(text, (10, ypos))
    #         ypos += 20