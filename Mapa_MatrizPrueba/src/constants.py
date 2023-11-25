import pygame
# Parametros
cellSize = 64
cellNum = 16
menuWidth = cellSize * 4

# Colores
lighGreen = pygame.Color('#ACE1AF')
darkGreen = pygame.Color('#03C03C')
grey = pygame.Color('#D3D3D3')
black = pygame.Color('#000000')

# Sprites
plantaSprite = pygame.transform.scale(pygame.image.load('assets/planta.png'), (cellSize, cellSize))
ovejaSprite = pygame.transform.scale(pygame.image.load('assets/oveja.png'), (cellSize, cellSize))
pumaSprite = pygame.transform.scale(pygame.image.load('assets/puma.png'), (cellSize, cellSize))

# Font
fontName = 'Minecraft'
# Sizes
h1Size = 32
pSize = 20

stats = {
    'puma':{
        'maxHp' : 150,
        'maxEnergy' : 80,
        'vel' : 2,
        'attack' : 50,
        'sprite' : pumaSprite,
        'attackRange' : 2 * cellSize,
        'visionRange' : 4 * cellSize,
        'dieta' : 'carnivoro',
        'especie' : 'puma',
    },
    'oveja':{
        'maxHp' : 100,
        'maxEnergy' : 50,
        'vel' : 1,
        'attack' : 10,
        'sprite' : ovejaSprite,
        'attackRange' : 0 * cellSize,
        'visionRange' : 2 * cellSize,
        'dieta' : 'herbivoro',
        'especie' : 'oveja',
    },
    'cabra':{},
    'conejo':{},
    'nandu':{},
    'zorro' :{},
    'condor':{},
}