import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("lluvia")

rain_color = (100, 150, 255)
raindrops = []

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(-height, 0)
        self.speed = random.uniform(1, 3)

    def fall(self):
        self.y += self.speed
 
    def draw(self):
        pygame.draw.line(screen, rain_color, (self.x, self.y), (self.x, self.y + 5), 1)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    raindrops.append(Raindrop()) # Añadir nuevas gotas de lluvia

    for drop in raindrops[:]:
        drop.fall()
        drop.draw()
        if drop.y > height:
            raindrops.remove(drop) # Eliminar gotas que han caído fuera de la pantalla

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()


