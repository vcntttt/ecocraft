import pygame, sys
from pygame.math import Vector2

from classes.animal import Animal
from classes.planta import Planta
from constants import *

pygame.init()
pygame.display.set_caption('ecocraft')

boardSurface = pygame.Surface((cellNum * cellSize, cellNum * cellSize))
menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))

screen = pygame.display.set_mode((cellNum * cellSize + menuWidth, cellNum * cellSize))

clock = pygame.time.Clock()

lionSprite = pygame.transform.scale(pygame.image.load('assets/lion.png'), (cellSize, cellSize))
plantaSprite = pygame.transform.scale(pygame.image.load('assets/planta.png'), (cellSize, cellSize))

lion = Animal(lionSprite)
org = Planta(plantaSprite)

def drawBoard(surface):
    for row in range (cellNum):
        for col in range (cellNum):
            if (row + col) % 2 == 0:
                color = lighGreen
            else:
                color = darkGreen
            pygame.draw.rect(surface, color, (col * cellSize, row * cellSize, cellSize, cellSize))

def initDisplay():
    drawBoard(boardSurface)
    menuSurface.fill(grey)
    
def drawDisplay():
    screen.blit(menuSurface, (cellNum * cellSize, 0))
    screen.blit(boardSurface, (0, 0))
organismos = []
def initOrganism():
    for i in range(10):
        animal = Animal(lionSprite)
        organismos.append(animal)
    for i in range(5):
        planta = Planta(plantaSprite)
        organismos.append(planta)
def drawOrganism():
    for org in organismos:
        org.draw(boardSurface)

initOrganism()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    initDisplay()
    drawOrganism()
    drawDisplay()
    pygame.display.update()
    clock.tick(60)