from classes.animal.animal import Animal  # Importa la clase Animal del modulo classes.animal.animal
from classes.animal.puma import Puma  # Importa la clase Puma del modulo classes.animal.puma
from classes.animal.condor import Condor  # Importa la clase Condor del módulo classes.animal.condor
from classes.animal.oveja import Oveja  # Importa la clase Oveja del módulo classes.animal.oveja
from classes.planta.planta import Planta  # Importa la clase Planta del módulo classes.planta.planta
from constants import *  # Importa constantes desde el archivo constants.py
from classes.animal.zorro import Zorro
from classes.animal.cocodrilo import Cocodrilo
import random
from classes.animal.conejo import Conejo
from classes.animal.nandu import Nandu
from classes.animal.cabra import Cabra
from classes.animal.gorreon import Gorreon
from classes.planta.paja import Paja
from classes.planta.amapola import Amapola
from classes.planta.matorral import Matorral
from classes.planta.girasol import Girasol
from classes.planta.juncos import Juncos
class Ecosistema:
    def __init__(self):
        self.orgsGroup = pygame.sprite.Group()  # Crea un grupo de sprites para almacenar los organismos del ecosistema
        self.initOrgs()  # Inicializa los organismos en el ecosistema
        self.initCSV()  # Inicializa los archivos CSV para registrar datos del ecosistema
        self.bornCount = 0  # Contador de nacimientos
        self.dieCount = 0  # Contador de muertes
        self.cicloCount = 0  # Contador de ciclos o turnos en el ecosistema

    def initOrgs(self):
        # Inicializa los organismos en el ecosistema
        carnivoros= [Puma,Zorro, Cocodrilo]
        herbivoros = [Oveja,Conejo,Nandu,Cabra, Gorreon]
        plantas = [Paja,Amapola,Matorral,Girasol,Juncos]
        for _ in range(2):
            animal = random.choice(carnivoros)(self)  # Crea instancias de Animal y las agrega al grupo de organismos
            self.orgsGroup.add(animal)
        for _ in range(8):
            animal = random.choice(herbivoros)(self)  # Crea instancias de Animal y las agrega al grupo de organismos
            self.orgsGroup.add(animal)
        for _ in range(6):
            planta = random.choice(plantas)(self)  # Crea instancias de Planta y las agrega al grupo de organismos
            self.orgsGroup.add(planta)
        
        condor = Condor(self)  # Crea una instancia de Condor y la agrega al grupo de organismos
        self.orgsGroup.add(condor)
        
    def update(self, gameHour):
        # Actualiza los organismos en el ecosistema segun la hora del juego
        for org in self.orgsGroup:
            if (isinstance(org, Animal)):
                org.detectOrgs(self.orgsGroup)  # Los animales detectan otros organismos
                org.detectOrgsToCoito(self.orgsGroup)  # Los animales detectan otros organismos para coito
            if isinstance(org, Planta):
                org.fotosintesis(gameHour)  # Las plantas realizan fotosintesis

    def initCSV(self):
        # Inicializa los archivos CSV para registrar datos del ecosistema
        with open('data/natalidad.csv', 'w') as file:
            file.write('ciclo,bornCount,dieCount\n')  # Encabezado para el archivo de natalidad

        with open('data/censo.csv', 'w') as file:
            file.write('ciclo,especie,cantidad\n')  # Encabezado para el archivo de censo

    def updateCSV(self):
        # Actualiza los archivos CSV con datos del ecosistema
        self.cicloCount += 1  # Incrementa el contador de ciclos
        with open('data/natalidad.csv', 'a') as file:
            file.write(f'{self.cicloCount},{self.bornCount},{self.dieCount}\n')  # Escribe datos de natalidad en el archivo

        with open('data/censo.csv', 'a') as file:
            for org in self.orgsGroup:
                if isinstance(org, Animal):
                    file.write(f'gola\n')  # Escribe datos de censo de animales en el archivo

    def newOrg(self, org):
        self.orgsGroup.add(org)  # Agrega un nuevo organismo al grupo del ecosistema
