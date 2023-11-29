import pygame
import pandas
import matplotlib.pyplot as plt
from constants import *

class Modal:
    def __init__(self):
        self.active = False  # Estado de la ventana modal (activa o inactiva)
        self.surface = pygame.Surface((int(visibleSize[0] / 1.5), int(visibleSize[1] / 1.5)))  # Superficie para la ventana modal
        self.surface.fill(white)  # Rellena la superficie con color blanco
        self.modalPos = ((visibleSize[0] - self.surface.get_width()) // 2, (visibleSize[1] - self.surface.get_height()) // 2)  # Posicion de la ventana modal en la pantalla

    def crearGraficoNatalidad(self):
        natalidadData = pandas.read_csv('data/natalidad.csv')  # Lee datos de un archivo CSV
        fig, ax = plt.subplots()  # Crea un grafico usando Matplotlib

        # Grafica los datos de nacimiento y muerte a lo largo del ciclo
        ax.plot(natalidadData['ciclo'], natalidadData['bornCount'], label='Nacimiento')
        ax.plot(natalidadData['ciclo'], natalidadData['dieCount'], label='Muerte')

        ax.set(xlabel='Ciclo')  # Etiqueta del eje x
        ax.set(ylabel='Conteo')  # Etiqueta del eje y
        ax.set_title('Natalidad y Mortalidad del Ecosistema')  # Titulo del grafico
        ax.legend()  # Muestra la leyenda del grafico

        plt.savefig('data/natalidad.png')  # Guarda el grafico como imagen PNG
        plt.close()  # Cierra el grafico
        self.grafico = pygame.image.load('data/natalidad.png')  # Carga la imagen del grafico para mostrar en la ventana modal

    def crearGraficoCenso(self):
        censoData = pandas.read_csv('data/censo.csv')  # Lee datos de un archivo CSV
        fig, ax = plt.subplots()  # Crea un grafico usando Matplotlib

        # Crea un grafico de barras con los datos de especies y su cantidad
        ax.bar(censoData['especie'], censoData['cantidad'])

        ax.set(xlabel='Especie')  # Etiqueta del eje x
        ax.set(ylabel='Conteo')  # Etiqueta del eje y
        ax.set_title('Censo del Ecosistema')  # Titulo del grafico

        plt.savefig('data/censo.png')  # Guarda el grafico como imagen PNG
        plt.close()  # Cierra el grafico
        self.grafico = pygame.image.load('data/censo.png')  # Carga la imagen del grafico para mostrar en la ventana modal

    def draw(self, screen):
        if self.active:  # Verifica si la ventana modal esta activa
            screen.blit(self.surface, (self.modalPos))  # Dibuja la superficie de la ventana modal en la pantalla
            self.surface.blit(self.grafico, (0, 0))  # Dibuja la imagen del grafico en la ventana modal

    def toggle(self, id):
        self.active = not self.active  # Cambia el estado de la ventana modal
        if self.active:
            if id == 0:
                self.crearGraficoNatalidad()  # Si se activa y el ID es 0, crea el grafico de natalidad
            elif id == 1:
                self.crearGraficoCenso()  # Si se activa y el ID es 1, crea el grafico de censo
