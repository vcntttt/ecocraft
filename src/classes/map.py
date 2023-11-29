import pygame
from classes.ecosistema import Ecosistema  # Importa la clase Ecosistema del módulo classes.ecosistema
from classes.menu import Menu  # Importa la clase Menu del modulo classes.menu
from constants import *  # Importa constantes desde el archivo constants.py
from classes.rain import Raindrop
class Map:
    def __init__(self, screen):
        self.screen = screen  # Establece la pantalla del juego
        self.fullMapSurface = pygame.Surface(mapSize)  # Crea una superficie para el mapa completo
        self.visibleSurface = self.fullMapSurface.subsurface(0, 0, visibleSize[0], visibleSize[1])  # Crea una superficie visible del mapa
        self.minimapSize = (180, 180)  # Tamaño del minimapa
        self.mmapPos = ((viewCellNum * cellSize) + 10, 200)  # Posicion del minimapa en la pantalla
        self.viewCoords = (0, 0)  # Coordenadas de vista del mapa
        self.matrix = map  # Matriz del mapa
        self.ecosistema = Ecosistema()  # Inicializa el ecosistema del juego
        self.menu = Menu(self.ecosistema, (viewCellNum * cellSize, 0))  # Crea el menu en la posición especificada
        self.loadMap()  # Carga el mapa inicial
        # Lluvia
        self.raindrops = []
        self.initRain()

    def loadMap(self):
        # Carga el mapa inicial basado en la matriz
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                cell = self.matrix[row][col]
                sprite = self.getSprite(cell)  # Obtiene el sprite correspondiente a la celda

                self.fullMapSurface.blit(sprite, (col * cellSize, row * cellSize))  # Dibuja el sprite en la superficie del mapa

    def getSprite(self, cell):
        # Obtiene el sprite según el tipo de celda en el mapa
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
        else:
            sprite = t1Sprite
        return sprite

    def updateMap(self, nMx, nMy):
        # Actualiza el area visible del mapa según la posicion del cursor en el minimapa
        xd = 0
        yd = 0
        if nMx in range(self.mmapPos[0], self.mmapPos[0] + self.minimapSize[0]):
            if nMy in range(self.mmapPos[1], self.mmapPos[1] + self.minimapSize[1]):
                xd = int(mapSize[0] * (nMx - self.mmapPos[0]) / self.minimapSize[0])
                yd = int(mapSize[1] * (nMy - self.mmapPos[1]) / self.minimapSize[1])
                xd = max(0, min(xd, self.fullMapSurface.get_width() - visibleSize[0]))
                yd = max(0, min(yd, self.fullMapSurface.get_height() - visibleSize[1]))
                self.visibleSurface = self.fullMapSurface.subsurface(xd, yd, visibleSize[0], visibleSize[1])

    def drawMinimap(self):
        # Dibuja el minimapa en la pantalla del juego
        minimapRect = pygame.Rect(self.mmapPos[0], self.mmapPos[1], self.minimapSize[0], self.minimapSize[1])
        pygame.draw.rect(self.screen, darkGreen, minimapRect)  # Dibuja un rectangulo para el minimapa en la pantalla

        # Dibuja los organismos del ecosistema en el minimapa
        for org in self.ecosistema.orgsGroup:
            xp = int(org.rect[0] / mapSize[0] * self.minimapSize[0] + self.mmapPos[0])
            yp = int(org.rect[1] / mapSize[1] * self.minimapSize[1] + self.mmapPos[1])
            spriteScaled = pygame.transform.scale(org.image, (20, 20))  # Escala el sprite del organismo para el minimapa
            self.screen.blit(spriteScaled, (xp, yp))  # Dibuja el sprite del organismo en el minimapa
    # Lluvia
    def initRain(self):
        print ("Init Rain")
        self.raindropsGroup = pygame.sprite.Group()
        for _ in range(10): #numero de gotas
            self.raindropsGroup.add(Raindrop())

    def updateRain(self):
        self.raindropsGroup.add(Raindrop())
        self.raindropsGroup.update()

    def draw(self, gameHour):
        # Dibuja elementos en la pantalla del juego
        self.loadMap()  # Carga el mapa
        self.menu.draw(self.screen)  # Dibuja el menu en la pantalla
        self.drawMinimap()  # Dibuja el minimapa
        self.menu.updateHour(gameHour)  # Actualiza la hora en el menu
        self.menu.updateStates(self.ecosistema.orgsGroup)  # Actualiza el estado de los organismos en el menu
        self.ecosistema.orgsGroup.draw(self.fullMapSurface)  # Dibuja los organismos en la superficie del mapa
        self.ecosistema.orgsGroup.update(self.ecosistema.orgsGroup)  # Actualiza los organismos
        self.ecosistema.update(gameHour)  # Actualiza el ecosistema según la hora del juego
        self.ecosistema.updateCSV()  # Actualiza el archivo CSV con los datos del ecosistema
        # Lluvia
        self.updateRain()
        self.raindropsGroup.draw(self.visibleSurface)
        # Actualizar
        self.screen.blit(self.visibleSurface, (0, 0))  # Dibuja la superficie visible del mapa en la pantalla