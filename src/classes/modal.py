import pygame
import pandas
import matplotlib.pyplot as plt
from constants import *

class Modal:
    def __init__(self):
        self.active = False
        self.surface = pygame.Surface((int(visibleSize[0] / 1.5), int(visibleSize[1] / 1.5)))
        self.surface.fill(white)
        self.modalPos = ((visibleSize[0] - self.surface.get_width()) //2, (visibleSize[1] - self.surface.get_height()) //2)

    def crearGraficoNatalidad(self):
        natalidadData = pandas.read_csv('data/natalidad.csv')
        fig, ax = plt.subplots()

        ax.plot(natalidadData['ciclo'], natalidadData['bornCount'], label='Nacimiento')
        ax.plot(natalidadData['ciclo'], natalidadData['dieCount'], label='Muerte')

        ax.set(xlabel='Ciclo')
        ax.set(ylabel='Conteo')
        ax.set_title('Natalidad y Mortalidad del Ecosistema')
        ax.legend()

        plt.savefig('data/natalidad.png')
        plt.close()
        self.grafico = pygame.image.load('data/natalidad.png')

    def crearGraficoCenso(self):
        censoData = pandas.read_csv('data/censo.csv')
        fig, ax = plt.subplots()

        ax.bar(censoData['especie'], censoData['cantidad'])

        ax.set(xlabel='Especie')
        ax.set(ylabel='Conteo')
        ax.set_title('Censo del Ecosistema')

        plt.savefig('data/censo.png')
        plt.close()
        self.grafico = pygame.image.load('data/censo.png')

    def draw (self,screen):
        if self.active:
            screen.blit(self.surface,(self.modalPos))
            self.surface.blit(self.grafico,(0,0))

    def toggle(self,id):
        self.active = not self.active
        if self.active:
            if id == 0:
                self.crearGraficoNatalidad()
            elif id == 1:
                self.crearGraficoCenso()