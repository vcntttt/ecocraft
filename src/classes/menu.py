import pygame
from classes.animal.animal import Animal
from constants import *

class Menu:
    def __init__(self,ecosistema):
        self.menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))
        self.menuSurface.fill(grey)
        self.h1Font = pygame.font.SysFont(fontName, h1Size)
        self.normalFont = pygame.font.SysFont(fontName, pSize)
        self.ecosistema = ecosistema

    def updateHour(self, gameHour):
        self.menuSurface.fill(grey)
        horaText = self.h1Font.render('Hora: ' + str(gameHour) + ':00', True, black)
        self.menuSurface.blit(horaText, (10, 10))
    
    def updateStates(self, organismos):
        ypos = 400
        bornText = self.normalFont.render((f'nacidos:{self.ecosistema.bornCount}'), True, black)
        dieText = self.normalFont.render((f'muertos:{self.ecosistema.dieCount}'), True, black)
        self.menuSurface.blit(bornText, (10, ypos))
        ypos += 30
        self.menuSurface.blit(dieText, (10, ypos))
        ypos += 30
        for org in organismos:
            if isinstance(org,Animal):
                genero = 'H' if org.genero == 0 else 'M'
            else:
                genero = 'P'
            if org.hp >= 0:
                string = (f"{org.__class__.__name__}{org.rect.topleft}({genero})({org.status}) - HP: {org.hp} - Energy: {org.energy}")
                orgText = self.normalFont.render(string, True, black)
                self.menuSurface.blit(orgText, (10, ypos))
                ypos += 30
                
    def draw(self, screen, position):
        screen.blit(self.menuSurface, position)