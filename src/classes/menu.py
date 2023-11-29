import pygame
from classes.animal.animal import Animal
from constants import *

class Menu:
    def __init__(self,ecosistema, position):
        self.menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))
        self.menuSurface.fill(grey)
        self.h1Font = pygame.font.SysFont(fontName, h1Size)
        self.normalFont = pygame.font.SysFont(fontName, pSize)
        self.ecosistema = ecosistema
        self.btnRect = pygame.Rect(10, 50, 220, 50)
        self.btnRect2 = pygame.Rect(10, 120, 220, 50)
        self.btnRect3 = pygame.Rect(240, 50, 220, 50)
        self.btnRect4 = pygame.Rect(240, 120, 220, 50)

        self.btnColor = lighBlue
        self.position = position

    def updateHour(self, gameHour):
        self.menuSurface.fill(grey)
        horaText = self.h1Font.render('Hora: ' + str(gameHour) + ':00', True, black)
        self.menuSurface.blit(horaText, (10, 10))
    
    def updateStates(self, organismos):
        ypos = 400
        bornText = self.normalFont.render((f'nacidos:{self.ecosistema.bornCount}'), True, black)
        dieText = self.normalFont.render((f'muertos:{self.ecosistema.dieCount}'), True, black)
        pygame.draw.rect(self.menuSurface, self.btnColor, self.btnRect)
        pygame.draw.rect(self.menuSurface, self.btnColor, self.btnRect2)
        pygame.draw.rect(self.menuSurface, self.btnColor, self.btnRect3)
        pygame.draw.rect(self.menuSurface, self.btnColor, self.btnRect4)
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
            
    def draw(self, screen):
        btnText = self.normalFont.render('Ver Grafico Natalidad/Mortalidad', True, black)
        btnText2 = self.normalFont.render('Ver Poblacion', True, black)
        textRect = btnText.get_rect(center=self.btnRect.center)
        textRect2 = btnText2.get_rect(center=self.btnRect2.center)
        self.menuSurface.blit(btnText, textRect)
        self.menuSurface.blit(btnText2, textRect2)
        screen.blit(self.menuSurface, self.position)