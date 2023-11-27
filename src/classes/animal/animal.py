import random
from pygame.math import Vector2
from classes.organismo import Organismo
from constants import *
from classes.planta.planta import Planta
class Animal(Organismo):
    def __init__(self,sprite, hp, nrg, nTrofico, attackRange, visionRange, attack, especie ,ecosistema ,speed=0.15, ):
        self.genero = random.randint(0,1) #0 para hembra y 1 para macho
        self.animationSpeed = speed
        self.isChasing = False
        self.isHiting = False
        self.isBeingChased = False
        self.target = None
        self.attackRange = attackRange
        self.visionRange = visionRange
        self.attack = attack
        self.especie = especie
        self.ecosistema = ecosistema
        self.isPregnant = False
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
            if org != self and org.isAlive:
                distance , direction = self.getDirection(org)
                if org.nivelTrofico == (self.nivelTrofico - 1):
                    if distance < self.visionRange:
                        self.target = org
                        self.chase(org,direction)
                        return

    def detectOrgsToCoito(self,orgs):
        for org in orgs:
            if org != self and org.isAlive:
                distance , direction = self.getDirection(org)
                if isinstance(org, Animal):
                    if self.genero != org.genero and self.especie == org.especie and (self.energy > 25 and org.energy > 25) and not (self.isPregnant or org.isPregnant):
                        if distance < self.visionRange * 2:
                            self.target = org
                            self.coito(org,direction)
                            return
    
    def coito(self,target,direction):
        from classes.animal.oveja import Oveja
        from classes.animal.puma import Puma
        couple = [self, target]
        for org in couple:
            if org.genero == 0:
                org.isPregnant = True

        self.rect.x += direction.x * 1
        self.rect.y += direction.y * 1 

        if pygame.sprite.collide_rect(self, target):
            if self.especie == 'puma':
                newAnimal = Puma(self.ecosistema)
            elif self.especie == 'oveja':
                newAnimal = Oveja(self.ecosistema)

            newAnimal.rect.topleft = self.rect.topleft
            newAnimal.isAlive = False
            newAnimal.isBorning = True
            self.ecosistema.newOrg(newAnimal)
            self.ecosistema.bornCount += 1
    
    def chase(self,target,direction):
        if not target.isAlive:
            self.target = None
            self.isChasing = False
            return
        self.isChasing = True
        target.isBeingChased = True
        self.rect.x += direction.x * 1
        self.rect.y += direction.y * 1

        if self.rect.colliderect(self.target.rect):
            self.targetAlcanzado(target)

    def targetAlcanzado(self,target):
        self.isChasing = False
        self.isHiting = True

    def attackTarget(self,target):
        if not target: return
        target.hp -= self.attack
        self.energy += (target.maxHp / 2)
        if target.hp <= 0:
            if isinstance(target, Planta):
                if target.enReposo: return
                target.die()
                self.ecosistema.dieCount += 1
                self.isHiting = False
                self.target = None

    def update(self, orgs):
        super().update(orgs)
        if self.isAlive:
            self.energy -= 0.5
            if self.energy <= 0:
                self.hp -= 1
                if self.hp <= 0:
                    self.die()
                    return
        else: return

        if self.isChasing:
            if self.target and self.getDirection(self.target)[0] > self.visionRange:
                self.isChasing = False
                self.target = None
            else:
                _, direction = self.getDirection(self.target)
                self.chase(self.target, direction)
        elif self.isHiting:
            if self.target and not self.target.isAlive:
                self.isHiting = False
                self.target = None
            else:
                self.attackTarget(self.target)
        else:
            self.move(orgs)