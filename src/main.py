import pygame, sys
from constants import *
from classes.map import Map

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ecocraft')
        self.screen = pygame.display.set_mode((cellNum * cellSize + menuWidth, cellNum * cellSize))
        self.clock = pygame.time.Clock()
        self.map = Map(self.screen)
        self.counter = 0
        self.gameHour = 0
        
    def run(self):
        while True:
            # Cerrar Ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Actualizar cosas
            self.counter += self.clock.tick(60)
            # Ciclos
            if self.counter >= 1000:
                self.gameHour += 1
                self.map.updateForTurn()
                self.counter = 0
                if self.gameHour == 24:
                    self.gameHour = 0
            self.map.update(self.gameHour)
            self.map.drawDisplay()
            pygame.display.update()

game = Game()
game.run()