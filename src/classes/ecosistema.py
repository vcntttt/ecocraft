from classes.animal.animal import Animal
from classes.animal.puma import Puma
from classes.animal.oveja import Oveja
from classes.planta.planta import Planta
from constants import *

class Ecosistema:
    def __init__(self):
        self.organismos = []
        self.initOrgs()
    # Organismos
    def initOrgs(self):
        self.organismos.extend([Puma() for i in range(2)])
        self.organismos.extend([Oveja() for i in range(8)])
        self.organismos.extend([Planta(plantaSprite) for i in range(6)])

    def updateOrganism(self):
        for org in self.organismos:
            if isinstance(org, Animal):
                org.move()
    
    def drawOrganism(self,surface):
        for org in self.organismos:
            org.draw(surface)