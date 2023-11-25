import pygame
from constants import *

class Menu:
    def __init__(self):
        self.menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))
        self.menuSurface.fill(grey)
        self.h1Font = pygame.font.SysFont(fontName, h1Size)
        self.normalFont = pygame.font.SysFont(fontName, pSize)

    def updateHour(self, gameHour):
        self.menuSurface.fill(grey)
        horaText = self.h1Font.render('Hora: ' + str(gameHour) + ':00', True, black)
        self.menuSurface.blit(horaText, (10, 10))
    
    def updateStates(self, organismos):
        ypos = 400
        for org in organismos:
            if org.hp >= 0:
                string = (f"{org.__class__.__name__}{org.rect.topleft} - HP: {org.hp} - Energy: {org.energy}")
                orgText = self.normalFont.render(string, True, black)
                self.menuSurface.blit(orgText, (10, ypos))
                ypos += 30
    
    def draw(self, screen, position):
        screen.blit(self.menuSurface, position)