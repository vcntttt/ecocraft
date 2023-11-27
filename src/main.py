import pygame
import sys
from constants import *
from classes.map import Map
from classes.rain import Gota

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ecocraft')
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.map = Map(self.screen)
        self.counter = 0
        self.counter2 = 0
        self.gameHour = 0
        self.time = 0
        

    def run(self):
        # gotas = [Gota() for _ in range(100)]  

        while True:
            # Cerrar Ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    nMx,nMy = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    self.map.updateMap(nMx,nMy)

            # for rain in gotas:
            #     rain.caida()  
            #     rain.show(self.screen)

            # Actualizar cosas
            self.time += self.clock.tick(30)
            self.counter += self.time
            self.counter2 += self.time

            # Ciclos
            if self.counter >= 5000:
                # self.gameHour += 1
                self.counter = 0
                if self.gameHour == 24:
                    self.gameHour = 0

            self.map.draw(self.gameHour)
            pygame.display.update()

game = Game()
game.run()