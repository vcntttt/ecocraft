import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Caida de Meteoritos')

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Cargar imagen del meteorito
meteorito_img = pygame.image.load('assets/m2.png')
meteorito_img = pygame.transform.scale(meteorito_img, (50, 50))  # Ajusta el tamaño como desees

# Lista de meteoritos con posiciones inicial y final
num_meteoritos = 5  # Cambia el número de meteoritos aquí
meteoritos = []
for _ in range(num_meteoritos):
    initial_x = 0  # Todos comienzan desde la esquina superior izquierda
    initial_y = 0  # Todos comienzan desde la esquina superior izquierda
    final_x = random.randint(WIDTH // 4, WIDTH * 3 // 4)  # Rango en el eje X hacia el centro
    final_y = random.randint(HEIGHT // 4, HEIGHT * 3 // 4)  # Rango en el eje Y hacia el centro
    meteoritos.append({
        'x': initial_x,
        'y': initial_y,
        'final_x': final_x,
        'final_y': final_y
    })

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for meteorito in meteoritos:
        # Calcular movimiento de cada meteorito
        meteorito['x'] += (meteorito['final_x'] - meteorito['x']) * 0.01
        meteorito['y'] += (meteorito['final_y'] - meteorito['y']) * 0.01

        # Dibujar cada meteorito
        screen.blit(meteorito_img, (meteorito['x'], meteorito['y']))

    pygame.display.flip()
    clock.tick(60)
