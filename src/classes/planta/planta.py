from classes.organismo import Organismo

class Planta (Organismo):
    def __init__(self,sprite):
        super().__init__(sprite, 50, 10, 0)