import pygame

# Parametros
cellSize = 64
cellNum = 15
menuWidth = cellSize * 5
resolution = (15 * cellSize + menuWidth, cellNum * cellSize)
mapSize = (cellNum * cellSize, cellNum * cellSize)

# Colores
lighGreen = pygame.Color('#ACE1AF')
darkGreen = pygame.Color('#03C03C')
grey = pygame.Color('#D3D3D3')
black = pygame.Color('#000000')
yellow = pygame.Color('#FFFF00')

# Sprites
def loadImg(path):
    return pygame.transform.scale(pygame.image.load(path), (cellSize, cellSize))

pumaSprite = loadImg('assets/puma.png')
ovejaSprite = loadImg('assets/oveja.png')
plantaSprite = loadImg('assets/planta.png')
condorSprite = loadImg('assets/condor.png')
arbolSprite = loadImg('assets/arbol.png')
tile1Sprite = loadImg('assets/tile1.jpg')
tile2Sprite = loadImg('assets/tile2.jpg')
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