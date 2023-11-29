from classes.organismo import Organismo  # Importa la clase Organismo del módulo classes.organismo
from classes.planta.semilla import Semilla  # Importa la clase Semilla del módulo classes.planta.semilla
from constants import *  # Importa constantes desde el archivo constants.py
import random

class Planta(Organismo):
    def __init__(self, sprite,hp,nrg ,ecosistema):
        # Inicializa una Planta en el ecosistema
        self.reproduccionNRG = 50  # Energia necesaria para la reproduccion
        self.reproduccionTime = 40  # Tiempo necesario para la reproduccion
        self.reproduccionProgress = 0  # Progreso actual de reproduccion
        self.ecosistema = ecosistema  # Asigna el ecosistema proporcionado
        super().__init__(sprite, hp, nrg, 0)  # Inicializa la clase base (Organismo) con ciertos parametros

    def fotosintesis(self, gameHour):
        # Método para simular la fotosintesis de la planta
        if minHrSol <= gameHour <= maxHrSol:  # Si la hora del juego está entre 10 y 19 horas
            self.energy += 5  # La planta incrementa su energia en 5 unidades durante la fotosintesis
            if self.energy >= self.reproduccionNRG:  # Si la energia alcanza el umbral para reproducirse
                self.energy = 5  # Restablece la energía a un valor inicial
                self.status = 'coitoVegano'  # Establece el estado de reproducción de la planta como 'coitoVegano'
                if random.random() < 0.5:  # Probabilidad del 50% para reproducirse
                    self.reproducir()  # Inicia el proceso de reproducción

    def reproducir(self):
        # Método para la reproduccion de la planta, creando nuevas semillas
        nSemillas = 1  # Cantidad de semillas a crear
        self.status = 'pregnat'  # Establece el estado de la planta como 'pregnat' durante la reproduccion
        for i in range(nSemillas):  # Para cada semilla a crear
            newSeed = Semilla(self.ecosistema)  # Crea una nueva instancia de Semilla con el ecosistema proporcionado
            # Establece una posición aleatoria cercana a la planta para la nueva semilla
            newSeed.rect.topleft = (
                self.rect.x + random.randint(-cellSize * 2, cellSize * 2),
                self.rect.y + random.randint(-cellSize * 2, cellSize * 2)
            )
            from classes.ecosistema import Ecosistema  # Importa la clase Ecosistema del modulo classes.ecosistema
            if isinstance(self.ecosistema, Ecosistema):  # Si el ecosistema es una instancia de Ecosistema
                self.ecosistema.newOrg(newSeed)  # Agrega la nueva semilla al ecosistema
            else:
                continue  # Continua con el siguiente ciclo si no es una instancia de Ecosistema
            self.ecosistema.bornCount += 1  # Incrementa el contador de nacimientos en el ecosistema
        self.finishReproduction()  # Finaliza el proceso de reproduccion

    def finishReproduction(self):
        # Metodo para finalizar el proceso de reproduccion de la planta
        self.status = 'alive'  # Restablece el estado de la planta como 'alive'
        if random.random() < 0.5:  # Probabilidad del 50% para morir después de la reproduccion
            self.die()  # Simula la muerte de la planta con una probabilidad del 50%

    def run(self, direction):
        pass  # Metodo vacio que representa una accion especifica para el movimiento de la planta (sin implementacion)
