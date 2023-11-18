import pygame
from constants import *
#menu
class Menu:
    def __init__(self, width, height):
        self.menuSurface = pygame.Surface((width, height))
        self.menuSurface.fill(grey)

    def updateHour(self, gameHour):
        self.menuSurface.fill(grey)
        h1Font = pygame.font.SysFont(self.fontName, 32)
        h1Text = h1Font.render('Hora: ' + str(gameHour) + ':00', True, black)
        self.menuSurface.blit(h1Text, (10, 10))

    def updateStates(self, organismos):
        ypos = 500
        for org in organismos:
            normalFont = pygame.font.SysFont(self.fontName, 14)
            normalText = normalFont.render('Organismo: ' + org.__class__.__name__, True, black)
            self.menuSurface.blit(normalText, (10, ypos))
            ypos += 30

    def draw(self, screen, position):
        screen.blit(self.menuSurface, position)

# map
class Map:
    def __init__(self,screen):
        self.screen = screen
        self.boardSurface = pygame.Surface((cellNum * cellSize, cellNum * cellSize))
        self.menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))
        self.ecosistema = Ecosistema()
        self.menu = Menu(menuWidth, cellNum * cellSize)
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

    def updateHour(self, gameHour):
        self.menu.updateHour(gameHour)

    def updateStates(self):
        self.menu.updateStates(self.ecosistema.organismos)
    def updateOrganism(self):
        self.ecosistema.updateOrganism()