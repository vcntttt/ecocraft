from classes.organismo import Organismo  # Importa la clase Organismo del modulo classes.organismo
from constants import *  # Importa constantes desde el archivo constants.py
import random

class Semilla(Organismo):
    def __init__(self, ecosistema):
        # Inicializa una Semilla dentro del ecosistema
        self.ecosistema = ecosistema  # Asigna el ecosistema proporcionado
        self.crecimientoTime = 40  # Tiempo necesario para el crecimiento de la semilla
        self.crecimientoProgress = 0  # Progreso actual de crecimiento de la semilla
        super().__init__(seedSprite, 1, 1, 0)  # Inicializa la clase base (Organismo) con ciertos parámetros
        self.status = 'seed'  # Establece el estado inicial de la semilla como 'semilla'

    def update(self, orgs):
        # Actualiza el estado de la semilla
        self.crecimientoProgress += 1  # Incrementa el progreso de crecimiento de la semilla
        self.drawBar(lighBlue, self.crecimientoProgress, self.crecimientoTime)  # Dibuja una barra de progreso visual
        if self.crecimientoProgress >= self.crecimientoTime:
            self.transformar()  # Si la semilla ha crecido por completo, realiza la transformación

    def transformar(self):
        # Método para transformar la semilla en una Planta
        from classes.planta.planta import Planta  # Importa la clase Planta del módulo classes.planta.planta
        if random.randint(0, 3) == 0:  # Realiza una elección aleatoria para la transformación
            newPlanta = Planta(self.ecosistema)  # Crea una nueva instancia de Planta con el ecosistema proporcionado
            newPlanta.rect.topleft = self.rect.topleft  # Establece la posición de la nueva planta
            self.ecosistema.newOrg(newPlanta)  # Agrega la nueva planta al ecosistema
            self.kill()  # Elimina la semilla
