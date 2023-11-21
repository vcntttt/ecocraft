from classes.animal.animal import Animal
from classes.organismo import Organismo
from classes.animal.puma import Puma
from classes.animal.oveja import Oveja
from classes.planta.planta import Planta
from classes.animal.carnivoro import Carnivoro
from constants import *

class Ecosistema:
    def __init__(self):
        self.orgsGroup = pygame.sprite.Group()
        self.initOrgs()
        
    def initOrgs(self):
        for i in range(2):
            animal = Puma()
            self.orgsGroup.add(animal)
        for i in range(8):
            animal = Oveja()
            self.orgsGroup.add(animal)
            planta = Planta(plantaSprite)
            self.orgsGroup.add(planta)

    def hunting(self, organismos):
        for org in organismos:
            if(isinstance(org, Carnivoro)):
                org.search(organismos)