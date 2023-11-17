from classes.organismo import Organismo

class Animal(Organismo):
    def __init__(self,sprite):
        super().__init__(sprite)
    def move(self):
        self.pos.x += self.vel