import pygame, sys

pygame.init()
pygame.display.set_caption('ecocraft')

cellSize = 50
cellNum = 15
menuWidth = cellSize * 5

lighGreen = (175,215,70)
darkGreen = (162,209,73)


boardSurface = pygame.Surface((cellNum * cellSize, cellNum * cellSize))
menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))

screen = pygame.display.set_mode((cellNum * cellSize + menuWidth, cellNum * cellSize))

clock = pygame.time.Clock()

def drawBoard(surface):
    for row in range (cellNum):
        for col in range (cellNum):
            if (row + col) % 2 == 0:
                color = lighGreen
            else:
                color = darkGreen
            pygame.draw.rect(surface, color, (col * cellSize, row * cellSize, cellSize, cellSize))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    drawBoard(boardSurface)
    menuSurface.fill(pygame.Color('lightblue'))
    screen.blit(boardSurface, (0, 0))
    screen.blit(menuSurface, (cellNum * cellSize, 0))
    
    pygame.display.update()
    clock.tick(60)