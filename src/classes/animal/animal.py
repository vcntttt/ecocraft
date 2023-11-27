import random
from pygame.math import Vector2
from classes.organismo import Organismo
from constants import *

class Animal(Organismo):
    def __init__(self,sprite, hp, nrg, nTrofico, attackRange, visionRange, attack, especie ,ecosistema ,speed=0.15, ):
        self.genero = random.randint(0,1) #0 para hembra y 1 para macho
        self.animationSpeed = speed
        self.isChasing = False
        self.isHiting = False
        self.target = None
        self.attackRange = attackRange
        self.visionRange = visionRange
        self.attack = attack
        self.especie = especie
        self.ecosistema = ecosistema
        super().__init__(sprite, hp, nrg, nTrofico)

    def move(self, orgs):
            movimiento = 4
            dx = random.choice([-1,0,1]) / movimiento
            dy = random.choice([-1,0,1]) / movimiento

            newX = self.rect.x + dx * cellSize
            newY = self.rect.y + dy * cellSize

            newX = max(0, min(newX, (cellNum - 1) * cellSize))
            newY = max(0, min(newY, (cellNum - 1) * cellSize))
            validMove = True
            newRect = self.rect.copy()
            newRect.topleft = (newX, newY)
            for animal in orgs:
                if animal != self and pygame.sprite.collide_rect(self, animal):
                    self.rect.x -= dx * cellSize
                    self.rect.y -= dy * cellSize
                    break

            if validMove:
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
        if self.energy == self.maxEnergy: return
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
                if self.genero != org.genero and self.especie == org.especie:
                    if distance < self.visionRange:
                        self.target = org
                        self.coito(org,direction)
                        return
    
    def coito(self,target,direction):
        pass
    
    def chase(self,target,direction):
        if not target.isAlive:
            self.target = None
            self.isChasing = False
            return
        self.isChasing = True
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
            target.die()
            self.isHiting = False
            self.target = None

    def update(self, orgs):
        super().update(orgs)
        if self.isAlive:
            self.energy -= 1
            if self.energy <= 0:
                self.hp -= 10
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