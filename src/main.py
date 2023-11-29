import pygame
import sys
from constants import *
from classes.map import Map
from classes.modal import Modal
# Se importan librería pygame, sys y se importan las clases de los demás archivos

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ecocraft')  # Establece el título de la ventana del juego como 'ecocraft'
        self.screen = pygame.display.set_mode(resolution)  # Crea la ventana del juego con las dimensiones definidas en 'resolution'
        self.clock = pygame.time.Clock()  # Inicializa un objeto Clock para controlar el tiempo del juego
        self.map = Map(self.screen)  # Crea un objeto Map para representar el mapa del juego
        self.counter = 0  # Inicializa un contador
        self.counter2 = 0  # Inicializa otro contador
        self.gameHour = 0  # Inicializa la hora del juego
        self.time = 0  # Inicializa el tiempo transcurrido
        self.modalWindow = Modal()  # Crea un objeto Modal para representar la ventana modal del juego
        
    def pausar(self):
        # Método para pausar el juego
        while True:
            e = pygame.event.wait()  # Espera un evento
            if e.type in (pygame.QUIT, pygame.KEYDOWN):  # Si se presiona la tecla 'P' se pausa
                return  # Sale del bucle de pausa
            
    def run(self):
        # Metodo principal para ejecutar el juego

        while True:
            # Manejo de eventos
            for event in pygame.event.get():  # Obtiene los eventos del juego
                if event.type == pygame.QUIT:  # Si se cierra la ventana
                    pygame.quit()  # Sale del juego
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                    if event.key == pygame.K_p:  # Si la tecla presionada es 'P'
                        self.pausar()  # Llama al método para pausar el juego
                if event.type == pygame.MOUSEMOTION:  # Si hay movimiento del mouse
                    nMx, nMy = event.pos  # Obtiene la posición del mouse

                if event.type == pygame.MOUSEBUTTONDOWN:  # Si se presiona un boton del mouse
                    # Verifica si se hizo clic en ciertos botones del menu y activa la ventana modal correspondiente
                    if self.map.menu.btnRect.collidepoint((event.pos[0] - self.map.menu.position[0], event.pos[1] - self.map.menu.position[1])):
                        self.modalWindow.toggle(0)  # Activa la ventana modal 0

                    if self.map.menu.btnRect2.collidepoint((event.pos[0] - self.map.menu.position[0], event.pos[1] - self.map.menu.position[1])):
                        self.modalWindow.toggle(1)  # Activa la ventana modal 1

                    if self.map.menu.btnRect3.collidepoint((event.pos[0] - self.map.menu.position[0], event.pos[1] - self.map.menu.position[1])):
                        self.map.toggleRain()  # Inicializa el efecto de lluvia
                        print(self.map.isRaining)
                        
            if self.modalWindow.active:  # Si la ventana modal está activa
                self.modalWindow.draw(self.screen)  # Dibuja la ventana modal en la pantalla del juego

            # Actualizacion del tiempo
            self.time += self.clock.tick(60)  # Controla el tiempo del juego a 60 FPS
            self.counter += self.time
            self.counter2 += self.time

            # Ciclos
            if self.counter >= 5000:  # Cada 5000 unidades de tiempo
                self.gameHour += 1  # Incrementa la hora del juego
                self.counter = 0
                if self.gameHour == 24:  # Si la hora del juego alcanza 24 (fin del día)
                    self.gameHour = 0  # Reinicia la hora del juego
            self.map.draw(self.gameHour)  # Dibuja el mapa basado en la hora actual del juego
            self.modalWindow.draw(self.screen)  # Dibuja la ventana modal en la pantalla del juego
            pygame.time.wait(300)  # Espera 300 milisegundos
            pygame.display.update()  # Actualiza la pantalla

game = Game()  # Crea una instancia del juego
game.run()  # Ejecuta el bucle principal del juego
