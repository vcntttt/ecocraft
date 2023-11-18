import pygame
# Parametros
cellSize = 50
cellNum = 20
menuWidth = cellSize * 5
fontName = 'Comic Sans MS'
# Colores
lighGreen = pygame.Color('#ACE1AF')
darkGreen = pygame.Color('#03C03C')
grey = pygame.Color('#D3D3D3')
black = pygame.Color('#000000')
# Sprites
plantaSprite = pygame.transform.scale(pygame.image.load('assets/planta.png'), (cellSize, cellSize))
ovejaSprite = pygame.transform.scale(pygame.image.load('assets/oveja.jpeg'), (cellSize, cellSize))
pumaSprite = pygame.transform.scale(pygame.image.load('assets/puma.jpeg'), (cellSize, cellSize))