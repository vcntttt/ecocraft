import pygame
from classes.ecosistema import Ecosistema
from classes.menu import Menu
from constants import *

class Map:
    def __init__(self,screen):
        self.screen = screen
        self.fullMapSurface = pygame.Surface(mapSize)
        self.visibleSurface = self.fullMapSurface.subsurface(0,0,visibleSize[0],visibleSize[1])
        self.minimapSize = (180,180)
        self.mmapPos = ((viewCellNum * cellSize) + 10,200)
        self.viewCoords = (0,0)
        self.matrix = map
        self.menu = Menu()
        self.ecosistema = Ecosistema()
        self.loadMap()

    def loadMap(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                cell = self.matrix[row][col]
                sprite = self.getSprite(cell)
                
                self.fullMapSurface.blit(sprite,(col * cellSize, row * cellSize))

    def getSprite(self,cell):
        if cell == 1:
            sprite = p1Sprite
        elif cell == 'r':
            sprite = rioSprite
        elif cell == 'r2':
            sprite = rio2Sprite
        elif cell == 'c1':
            sprite = c1Sprite
        elif cell == 'c2':
            sprite = c2Sprite
        elif cell == 'pd1':
            sprite = pd1Sprite
        else :sprite = t1Sprite
        return sprite
    
    def updateMap(self,nMx,nMy):
        xd=0 ; yd=0
        if nMx in range(self.mmapPos[0],self.mmapPos[0] + self.minimapSize[0]):
            if nMy in range(self.mmapPos[1],self.mmapPos[1] + self.minimapSize[1]):
                xd = int(mapSize[0] *(nMx - self.mmapPos[0]) / self.minimapSize[0])
                yd = int(mapSize[1] *(nMy - self.mmapPos[1]) / self.minimapSize[1])
                xd = max(0, min(xd, self.fullMapSurface.get_width() - visibleSize[0]))
                yd = max(0, min(yd, self.fullMapSurface.get_height() - visibleSize[1]))
                self.visibleSurface = self.fullMapSurface.subsurface(xd,yd,visibleSize[0],visibleSize[1])

    def drawMinimap(self):
        minimapRect = pygame.Rect(self.mmapPos[0],self.mmapPos[1],self.minimapSize[0],self.minimapSize[1])
        pygame.draw.rect(self.screen,darkGreen,minimapRect)
        
    def draw(self,gameHour):
        self.screen.blit(self.visibleSurface,(0,0))
        self.menu.draw(self.screen, (viewCellNum * cellSize, 0))
        self.drawMinimap()
        self.menu.updateHour(gameHour)
        # self.menu.updateStates(self.ecosistema.orgsGroup)
        # self.ecosistema.update()
        self.ecosistema.orgsGroup.draw(self.fullMapSurface)
        # self.ecosistema.orgsGroup.update(self.ecosistema.orgsGroup)