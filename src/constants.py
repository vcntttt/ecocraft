import pygame
# Parametros
cellSize = 64
cellNum = 15
menuWidth = cellSize * 5

# Colores
lighGreen = pygame.Color('#ACE1AF')
darkGreen = pygame.Color('#03C03C')
grey = pygame.Color('#D3D3D3')
black = pygame.Color('#000000')

# Sprites
plantaSprite = pygame.transform.scale(pygame.image.load('assets/planta.png'), (cellSize, cellSize))
ovejaSprite = pygame.transform.scale(pygame.image.load('assets/oveja.png'), (cellSize, cellSize))
pumaSprite = pygame.transform.scale(pygame.image.load('assets/puma.png'), (cellSize, cellSize))
tile1Sprite = pygame.transform.scale(pygame.image.load('assets/tile1.jpg'), (cellSize, cellSize))
tile2Sprite = pygame.transform.scale(pygame.image.load('assets/tile2.jpg'), (cellSize, cellSize))

# Font
fontName = 'Minecraft'
# Sizes
h1Size = 32
pSize = 24

stats = {
    'puma':{
        'hp' : 150,
        'energy' : 80,
        'vel' : 2,
        'attack' : 50,
        'sprite' : pumaSprite,
        'attackRange' : 2,
        'visionRange' : 4,
        'especie' : 'puma',
    }, 
    'oveja':{
        'hp' : 100,
        'energy' : 50,
        'vel' : 1,
        'attack' : 10,
        'sprite' : ovejaSprite,
        'attackRange' : 0,
        'especie' : 'oveja',
    },
    'cabra':{},
    'conejo':{},
    'zorro' :{},
    'nandu':{},
    'condor':{},
}