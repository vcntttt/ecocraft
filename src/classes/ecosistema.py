from classes.animal.animal import Animal
from classes.organismo import Organismo
from classes.animal.puma import Puma
from classes.animal.oveja import Oveja
from classes.planta.planta import Planta
from constants import *

class Ecosistema:
    def __init__(self):
        self.orgsGroup = pygame.sprite.Group()
        self.initOrgs()
    # Organismos
    def initOrgs(self):
        for i in range (8):
            animal = Animal(pumaSprite)
            self.orgsGroup.add(animal)