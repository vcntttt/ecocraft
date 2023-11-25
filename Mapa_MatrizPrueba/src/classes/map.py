import pygame
from classes.ecosistema import Ecosistema
from classes.menu import Menu

class Map:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 900, 800
        self.CELL_SIZE = 50

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.image_path_1 = './assets/tile1.jpg'
        self.image_path_2 = './assets/tile2.jpg'

        self.image_1 = pygame.transform.scale(pygame.image.load(self.image_path_1), (self.CELL_SIZE, self.CELL_SIZE))
        self.image_2 = pygame.transform.scale(pygame.image.load(self.image_path_2), (self.CELL_SIZE, self.CELL_SIZE))

        self.matrix = [[self.image_1 if (i + j) % 2 == 0 else self.image_2 for j in range(45)] for i in range(45)]

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('ecocraft')

        self.menu = Menu()  # Inicializar la instancia de Menu
        self.ecosistema = Ecosistema()  # Inicializar la instancia de Ecosistema

    def draw_matrix(self):
        for y, row in enumerate(self.matrix):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * self.CELL_SIZE, y * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                self.screen.blit(cell, rect.topleft)

    def map_run(self):
        running = True
        while running:
            self.screen.fill(self.WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_matrix()

            pygame.display.flip()
        pygame.quit()

    def update(self, gameHour):
        self.menu.updateHour(gameHour)
        self.menu.updateStates(self.ecosistema.orgsGroup)
        self.ecosistema.update()

    def updateForTurn(self):
        self.ecosistema.orgsGroup.update()
        pass
