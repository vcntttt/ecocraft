import pygame
from constants import *

class Menu:
    def __init__(self):
        self.menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))
        self.menuSurface.fill(grey)
    
    def updateHour(self, gameHour):
        self.menuSurface.fill(grey)
        h1Font = pygame.font.SysFont(fontName, 32)
        h1Text = h1Font.render('Hora: ' + str(gameHour) + ':00', True, black)
        self.menuSurface.blit(h1Text, (10, 10))
    
    def updateStates(self, organismos):
        ypos = 500
        for org in organismos:
            normalFont = pygame.font.SysFont(fontName, 14)
            string = 'Organismo: ' + org.__class__.__name__ + str(org.pos)
            normalText = normalFont.render(string, True, black)
            self.menuSurface.blit(normalText, (10, ypos))
            ypos += 30
    
    def draw(self, screen, position):
        screen.blit(self.menuSurface, position)