from classes.organismo import Organismo
from constants import *

class Ecosistema:
    def __init__(self):
        self.ambiente = []
        self.ambiente.append(Organismo(lionSprite))
        self.ambiente.append(Organismo(plantaSprite))