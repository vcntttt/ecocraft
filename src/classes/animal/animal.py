import random
from pygame.math import Vector2
from classes.organismo import Organismo
from constants import *
# tiene que cazar, descomponerse y morir
class Animal(Organismo):
    def __init__(self,sprite, hp, nrg, nTrofico, attackRange, visionRange):
        self.genero = random.randint(0,1) #0 para hembra y 1 para macho
        self.animationSpeed = 1
        self.isChasing = False
        self.isHiting = False
        self.target = None
        self.attackRange = attackRange
        self.visionRange = visionRange
        super().__init__(sprite, hp, nrg, nTrofico)

    def move(self):
        self.energy -= 10
        if self.energy <= 0:
            print("die")
            # self.die()
            return
        dx = random.choice([-self.animationSpeed,0,self.animationSpeed])
        dy = random.choice([-self.animationSpeed,0,self.animationSpeed])
        
        newX = self.rect.x + dx * cellSize
        newY = self.rect.y + dy * cellSize

        newX = max(0, min(newX, (cellNum - 1) * cellSize))
        newY = max(0, min(newY, (cellNum - 1) * cellSize))

        self.rect.topleft = (newX, newY)

    def getDirection(self,org):
        enemyVector = Vector2(org.rect.center)
        myVector = Vector2(self.rect.center)
        distance = (enemyVector - myVector).magnitude()
        if distance > 0:
            direction = (enemyVector - myVector).normalize()
        else:
            direction = Vector2()

        return distance, direction
    
    def detectOrgs(self,orgs):
        if self.energy == self.maxEnergy: return
        for org in orgs:
            if org != self:
                distance , direction = self.getDirection(org)
                if org.nivelTrofico < (self.nivelTrofico - 1):
                    if distance < self.visionRange:
                        self.chase(org,direction)
                        return
                
    def chase(self,target,direction):
        self.target = target
        self.isChasing = True
        self.rect.x += direction.x * self.animationSpeed
        self.rect.y += direction.y * self.animationSpeed

        if self.rect.colliderect(self.target.rect):
            self.targetAlcanzado(target)

    def targetAlcanzado(self,target):
        self.isChasing = False
        self.target = None

    def attack(self,target):
        target.hp -= 50
        if target.hp <= 0:
            target.die()

    def gainEnergy(self, nrg):
        self.energy += nrg

    def update(self):
        if self.isChasing:
            if self.target and self.getDirection(self.target)[0] > self.visionRange:
                self.isChasing = False
                self.target = None
            else:
                _, direction = self.getDirection(self.target)
                self.chase(self.target, direction)
        else:
            self.move()