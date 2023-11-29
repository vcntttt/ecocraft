import random
from constants import *

class Organismo(pygame.sprite.Sprite):
    posiciones = set()  # Conjunto para almacenar posiciones de organismos

    def __init__(self, sprite, hp, nrg, nTrofico):
        super().__init__()
        # pygame sprites
        self.image = sprite  # Imagen del organismo
        self.rect = self.image.get_rect()  # Rectángulo que representa el organismo en la pantalla
        # stats
        self.hp = hp  # Puntos de vida del organismo
        self.maxHp = hp  # Puntos de vida maximos
        self.energy = nrg  # Energia del organismo
        self.maxEnergy = nrg  # Energia maxima
        self.nivelTrofico = nTrofico  # Nivel trofico del organismo
        # states
        self.status = 'alive'  # Estado del organismo (vivo)
        self.borningTime = 25  # Tiempo de nacimiento
        self.borningProgress = 0  # Progreso de nacimiento
        self.decompositionTime = 20  # Tiempo de descomposición
        self.decompositionProgress = 0  # Progreso de descomposición
        self.originalImg = sprite.copy()  # Copia de la imagen original del organismo

        # Asignación de una posicion aleatoria que no esté ocupada por otro organismo
        while True:
            newPos = (random.randint(0, cellNum - 1) * cellSize, random.randint(0, cellNum - 1) * cellSize)
            if newPos not in self.posiciones:
                self.posiciones.add(newPos)
                break
        self.rect.topleft = newPos  # Establece la posicion del organismo en la pantalla

    def die(self):
        # Metodo para indicar que el organismo ha muerto y comenzar la descomposicion
        self.status = 'descomposing'  # Cambia el estado a 'descomponiendose'
        # Crea una imagen gris para representar la descomposición del organismo
        greyImg = pygame.Surface(self.image.get_size())
        greyImg = greyImg.convert_alpha()
        for x in range(greyImg.get_width()):
            for y in range(self.image.get_height()):
                red, green, blue, alpha = self.image.get_at((x, y))
                grey = (red + green + blue) // 3  # Escala de grises
                greyImg.set_at((x, y), (grey, grey, grey, alpha))
        self.image = greyImg  # Establece la nueva imagen del organismo como gris

    def update(self, orgs):
        # Metodo de actualizacion del organismo (verifica la descomposicion)
        if self.status == 'descomposing':
            self.decompositionProgress += 1  # Incrementa el progreso de descomposicion
            # Dibuja una barra amarilla para indicar el progreso de descomposición
            self.drawBar(yellow, self.decompositionProgress, self.decompositionTime)
            if self.decompositionProgress >= self.decompositionTime:
                # Si el organismo esta completamente descompuesto, reemplaza por otro organismo
                from classes.animal.animal import Animal
                from classes.planta.planta import Planta
                if isinstance(self, Animal):  # Si el organismo es un animal, reemplazalo con una planta
                    newPlant = Planta(plantaSprite)
                    newPlant.rect.topleft = self.rect.topleft
                    orgs.add(newPlant)
                self.kill()  # Elimina el organismo actual

    def drawBar(self, color, param, total):
        # Metodo para dibujar una barra de progreso en la imagen del organismo
        barWidth = self.rect.width * (param / total)  # Calcula el ancho de la barra
        barHeight = 10  # Altura de la barra
        bar = pygame.Surface((barWidth, barHeight))  # Crea una superficie para la barra
        bar.fill(color)  # Rellena la barra con un color específico

        decomImg = self.image.copy()  # Copia la imagen actual del organismo
        barPos = (0, self.rect.height - barHeight)  # Posicion de la barra en la imagen
        decomImg.blit(bar, barPos)  # Une la barra con la imagen del organismo
        self.image = decomImg  # Actualiza la imagen del organismo con la barra
