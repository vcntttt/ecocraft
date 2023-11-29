import pygame
import sys
from constants import *
from classes.map import Map
from classes.rain import Gota
from classes.modal import Modal
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
        self.modalWindow = Modal()
        
    def pausar(self):
        while True:
            e = pygame.event.wait()
            if e.type in (pygame.QUIT, pygame.KEYDOWN):
                return
            
    def run(self):
        # gotas = [Gota() for _ in range(100)]  

        while True:
            # Cerrar Ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pausar()
                if event.type == pygame.MOUSEMOTION:
                    nMx,nMy = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    self.map.updateMap(nMx,nMy)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.map.menu.btnRect.collidepoint((event.pos[0] - self.map.menu.position[0], event.pos[1] - self.map.menu.position[1])):
                        self.modalWindow.toggle(0)
                        print('btn clicked')
                    if self.map.menu.btnRect2.collidepoint((event.pos[0] - self.map.menu.position[0], event.pos[1] - self.map.menu.position[1])):
                        self.modalWindow.toggle(1)
                        print('btn clicked')

            if self.modalWindow.active:
                    self.modalWindow.draw(self.screen)

            # Actualizar cosas
            self.time += self.clock.tick(60)
            self.counter += self.time
            self.counter2 += self.time

            # Ciclos
            if self.counter >= 5000:
                self.gameHour += 1
                self.counter = 0
                if self.gameHour == 24:
                    self.gameHour = 0
            self.map.draw(self.gameHour)
            self.modalWindow.draw(self.screen)
            pygame.time.wait(300)
            pygame.display.update()

game = Game()
game.run()