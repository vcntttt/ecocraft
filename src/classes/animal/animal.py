import random
from pygame.math import Vector2
from classes.organismo import Organismo
from constants import *
from classes.planta.planta import Planta
from classes.planta.semilla import Semilla
#estados:
# 1. alive
# 2. descomposing
# 3 pregnat
# 4. chasing
# 5. being chased
# 6. borning
# 4. dead

class Animal(Organismo):
    def __init__(self,sprite, hp, nrg, nTrofico, attackRange, visionRange, attack, especie ,ecosistema ,speed=0.15, ):
        self.genero = random.randint(0,1) #0 para hembra y 1 para macho
        self.animationSpeed = speed
        self.target = None
        self.attackRange = attackRange
        self.visionRange = visionRange
        self.attack = attack
        self.especie = especie
        self.ecosistema = ecosistema
        # coito extras
        self.gestationTime = 50
        self.gestationProgress = 0
        self.coitoCooldown = 100
        self.coitoProgress = 0
        #init del organismo
        super().__init__(sprite, hp, nrg, nTrofico)

    def move(self, orgs):
            dx = random.choice([-1,0,1])  
            dy = random.choice([-1,0,1]) 

            newX = self.rect.x + dx * cellSize
            newY = self.rect.y + dy * cellSize

            newX = max(0, min(newX, (cellNum - 1) * cellSize))
            newY = max(0, min(newY, (cellNum - 1) * cellSize))
            
            self.rect.topleft = (newX, newY)

    def getDirection(self, org):
        enemyVector = Vector2(org.rect.center)
        myVector = Vector2(self.rect.center)
        distance = (enemyVector - myVector).magnitude()
        if distance > 0:
            direction = (enemyVector - myVector).normalize()
        else:
            direction = Vector2()

        return distance, direction
    
    def detectOrgs(self,orgs):
        if self.energy >= self.maxEnergy: return
        for org in orgs:
            if org != self and org.status == 'alive' and self.status == 'alive':
                distance , direction = self.getDirection(org)
                if org.nivelTrofico == (self.nivelTrofico - 1):
                    if distance < self.visionRange:
                        self.target = org
                        self.status = 'chasing'
                        self.target.run(direction)
                        return

    def detectOrgsToCoito(self,orgs):
        for org in orgs:
            if org != self and org.status == 'alive' and self.status == 'alive':
                distance , direction = self.getDirection(org)
                if isinstance(org, Animal):
                    if self.genero != org.genero and self.especie == org.especie and (self.energy > 25 and org.energy > 25) and org.status == 'alive' and not self.status == 'pregnat':
                        if distance < self.visionRange * 2:
                            self.target = org
                            self.coito(org,direction)
                            return
    
    def coito(self,target,direction):
        
        couple = [self, target]
        self.rect.x += direction.x * 1
        self.rect.y += direction.y * 1 

        if pygame.sprite.collide_rect(self, target):
            for org in couple:
                if org.genero == 0:
                    org.status = 'pregnat'
            self.gestationProgress = 0
            self.coitoProgress = self.coitoCooldown

    def chase(self,direction):
        self.rect.x += direction.x * cellSize
        self.rect.y += direction.y * cellSize

        if self.attackRange >= self.getDirection(self.target)[0]:
            self.status = 'hiting'

    def run(self,direction):
        dx = -direction[0]
        dy = -direction[1]

        newX = self.rect.x + dx * cellSize
        newY = self.rect.y + dy * cellSize
        newX = max(0, min(newX, (cellNum - 1) * cellSize))
        newY = max(0, min(newY, (cellNum - 1) * cellSize))
        
        self.rect.topleft = (newX, newY)

    def attackTarget(self):
        self.target.hp -= self.attack
        self.energy += min(self.target.maxHp/2,self.maxEnergy-self.energy)
        if self.target.hp <= 0:
                self.target.die()
                self.ecosistema.dieCount += 1
                if isinstance(self.target, Planta):
                    especie = 'planta'
                else: especie = self.target.especie
                print(f'{self.especie} kill {especie}')
                self.status = 'alive'
                self.target = None

    def newAnimal(self):
        from classes.animal.oveja import Oveja
        from classes.animal.puma import Puma
        from classes.animal.condor import Condor
        if self.especie == 'puma':
            newAnimal = Puma(self.ecosistema)
        elif self.especie == 'oveja':
            newAnimal = Oveja(self.ecosistema)
        elif self.especie == 'condor':
            newAnimal = Condor(self.ecosistema)
        else:
            return
        newAnimal.rect.topleft = self.rect.topleft
        newAnimal.status = 'borning'
        self.ecosistema.newOrg(newAnimal)
        self.ecosistema.bornCount += 1

    def update(self, orgs):
        super().update(orgs)
        if self.status == 'alive':
            self.energy -= 0.5
            if self.energy <= 0:
                self.hp -= 1
                if self.hp <= 0:
                    self.die()
                    self.ecosistema.dieCount += 1

        if self.status == 'chasing':
            _, direction = self.getDirection(self.target)
            self.chase(direction)
                
        elif self.status == 'hiting':
            if not self.target:
                self.target = None
                self.status = 'alive'
            else:
                self.attackTarget()

        elif self.status == 'borning':
            self.borningProgress += 1
            self.drawBar(red, self.borningProgress, self.borningTime)
            if self.borningProgress >= self.borningTime:
                self.status = 'alive'
                self.image = self.originalImg
            return
        elif self.status == 'pregnat':
            self.gestationProgress += 1
            self.drawBar(orange, self.gestationProgress, self.gestationTime)
            if self.gestationProgress >= self.gestationTime:
                self.newAnimal()
                self.status = 'alive'
                self.gestationProgress = 0
                self.image = self.originalImg
                return
            if self.coitoCooldown > 0:
                self.coitoCooldown -= 1
            return
        elif self.status == 'descomposing':
            return
        elif self.status == 'alive':
            self.move(orgs)