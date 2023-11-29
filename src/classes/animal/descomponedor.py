from classes.animal.animal import Animal

class Descomponedor(Animal):
    def __init__(
            self,
            sprite, 
            hp, 
            nrg, 
            attackRange, 
            visionRange, 
            attack, 
            especie, 
            ecosistema,
            speed=0.15):
        
        super().__init__(
            sprite, 
            hp, 
            nrg, 
            3, #nTrofico
            attackRange, 
            visionRange, 
            attack, 
            especie, 
            ecosistema,
            speed)
        
    def detectOrgs(self, orgs):
            for org in orgs:
                if org != self and org.status == 'descomposing':
                    distance, direction = self.getDirection(org)
                    if distance < self.visionRange:
                        self.target = org
                        self.status = 'chasing'
                        return