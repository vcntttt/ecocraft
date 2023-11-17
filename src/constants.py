import pygame
# Parametros
cellSize = 50
cellNum = 20
menuWidth = cellSize * 5

# Colores
lighGreen = pygame.Color('#ACE1AF')
darkGreen = pygame.Color('#03C03C')
grey = pygame.Color('#D3D3D3')

# Sprites
lionSprite = pygame.transform.scale(pygame.image.load('assets/lion.png'), (cellSize, cellSize))
plantaSprite = pygame.transform.scale(pygame.image.load('assets/planta.png'), (cellSize, cellSize))