import pygame

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colores
WHITE = (255, 255, 255)

# Cargar la imagen del sol
sun_image = pygame.image.load('assets/sun.png')  
sun_image = pygame.transform.scale(sun_image, (100, 100))  # Escalar la imagen a un tamaño x

# Posicion inicial del sol
sun_x = 0 - sun_image.get_width()
sun_y = 0  # Centrado verticalmente

# Velocidad del sol
sun_speed = 3

clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover el sol de izquierda a derecha
    sun_x += sun_speed
    if sun_x > WIDTH:
        sun_x = 0 - sun_image.get_width()  # Reiniciar la posición del sol al salir de la pantalla

    # Dibujar el sol en la pantalla
    SCREEN.blit(sun_image, (sun_x, sun_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
