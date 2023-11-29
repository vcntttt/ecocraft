import pygame
from classes.animal.animal import Animal  # Importa la clase Animal del paquete classes.animal
from constants import *  # Importa constantes desde el archivo constants.py

class Menu:
    def __init__(self, ecosistema, position):
        self.menuSurface = pygame.Surface((menuWidth, cellNum * cellSize))  # Crea una superficie para el menu
        self.menuSurface.fill(grey)  # Rellena la superficie con color gris
        self.h1Font = pygame.font.SysFont(fontName, h1Size)  # Establece una fuente para encabezados
        self.normalFont = pygame.font.SysFont(fontName, pSize)  # Establece una fuente normal
        self.ecosistema = ecosistema  # Almacena una referencia al ecosistema del juego
        # Define botones rectangulares en el menu
        self.btnRect = pygame.Rect(10, 50, 220, 50)
        self.btnRect2 = pygame.Rect(10, 120, 220, 50)
        self.btnRect3 = pygame.Rect(240, 50, 220, 50)
        self.btnRect4 = pygame.Rect(240, 120, 220, 50)
        self.btnColor = lighBlue  # Color de los botones
        self.position = position  # Posición del menu en la pantalla

    def updateHour(self, gameHour):
        # Actualiza la hora en el menu
        self.menuSurface.fill(grey)  # Limpia el menu
        horaText = self.h1Font.render('Hora: ' + str(gameHour) + ':00', True, black)  # Renderiza la hora
        self.menuSurface.blit(horaText, (10, 10))  # Dibuja la hora en la superficie del menu

    def updateStates(self, organismos):
        # Actualiza los estados de los organismos y muestra información en el menu
        ypos = 400  # Posicion Y inicial
        bornText = self.normalFont.render((f'nacidos:{self.ecosistema.bornCount}'), True, black)  # Renderiza el conteo de nacimientos
        dieText = self.normalFont.render((f'muertos:{self.ecosistema.dieCount}'), True, black)  # Renderiza el conteo de muertes
        # Dibuja rectangulos para los botones
        pygame.draw.rect(self.menuSurface, self.btnColor, self.btnRect)
        pygame.draw.rect(self.menuSurface, self.btnColor, self.btnRect2)
        pygame.draw.rect(self.menuSurface, self.btnColor, self.btnRect3)
        pygame.draw.rect(self.menuSurface, self.btnColor, self.btnRect4)
        self.menuSurface.blit(bornText, (10, ypos))  # Dibuja el texto de nacimientos en el menu
        ypos += 30
        self.menuSurface.blit(dieText, (10, ypos))  # Dibuja el texto de muertes en el menu
        ypos += 30
        for org in organismos:
            if isinstance(org, Animal):  # Verifica si el organismo es un animal
                genero = 'H' if org.genero == 0 else 'M'  # Establece el genero del animal
            else:
                genero = 'P'  # Si no es un animal, se asume que es una planta
            if org.hp >= 0:  # Verifica si el organismo tiene puntos de vida
                # Crea una cadena de texto con información sobre el organismo
                string = (f"{org.__class__.__name__}{org.rect.topleft}({genero})({org.status}) - HP: {org.hp} - Energy: {org.energy}")
                orgText = self.normalFont.render(string, True, black)  # Renderiza la informacion del organismo
                self.menuSurface.blit(orgText, (10, ypos))  # Dibuja la informacion del organismo en el menu
                ypos += 30

    def draw(self, screen):
        # Dibuja los botones en el menu en la pantalla del juego
        btnText = self.normalFont.render('Ver Grafico Natalidad/Mortalidad', True, black)  # Texto para el botón 1
        btnText2 = self.normalFont.render('Ver Poblacion', True, black)  # Texto para el botón 2
        textRect = btnText.get_rect(center=self.btnRect.center)  # Posicion del texto del botón 1
        textRect2 = btnText2.get_rect(center=self.btnRect2.center)  # Posicion del texto del botón 2
        self.menuSurface.blit(btnText, textRect)  # Dibuja el texto del botón 1 en la superficie del menu
        self.menuSurface.blit(btnText2, textRect2)  # Dibuja el texto del botón 2 en la superficie del menu
        screen.blit(self.menuSurface, self.position)  # Dibuja el menu en la pantalla del juego
