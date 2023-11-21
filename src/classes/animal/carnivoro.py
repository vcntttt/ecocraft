from classes.animal.animal import Animal
from classes.animal.herviboro import Herviboro
import math
class Carnivoro(Animal):
    def __init__(self,sprite):
        super().__init__(sprite)
        self.dieta = 1

    def search(self, organismos):
        for org in organismos:
            if (isinstance(org, Herviboro)):
                dx = self.rect.topleft[0] - org.rect.topleft[0]
                dy = self.rect.topleft[1] - org.rect.topleft[1]
                distance = math.hypot(dx, dy)
                if distance < 200 and org.hp > 0:
                    self.hunt(org)
                
    def hunt(self, org):
        org.hp -= 50
        if org.hp <= 0:
            org.kill()