import pygame, sys
from pygame.locals import *
from globalDefs import *
class Bear:
    def __init__(self):
        self.BearPic = pygame.image.load('spacebear.jpg')
        self.laser = pygame.image.load('laser.jpg')
        self.chargedBear = pygame.image.load('Bearbeam.png')
        self.antiBear = pygame.image.load('Bearnegbeam.png')
        self.laserdis = 50
        self.kitMove = 15
        self.laserFire = False
        self.kitCharge = 0
        self.kitNegCharge = 0
        self.laserMod = pygame.transform.scale(self.laser, (2000,20 + self.kitCharge))
        self.laserMod = pygame.transform.scale(self.laser, (2000,20 + self.kitCharge))
        self.kitRect = self.BearPic.get_rect()
        self.laserRect = self.laserMod.get_rect()
        self.moveUp = False
        self.moveDown = False

    def chargeBear(self, windowSurface):
        kitRect = self.kitRect
        kitCharge = self.kitCharge
        chargedBear = pygame.transform.scale(self.chargedBear, (kitRect.width + kitCharge, kitRect.height + kitCharge))
        chargeBearRect = chargedBear.get_rect()
        chargeBearRect.center = kitRect.center
        windowSurface.blit(chargedBear, chargeBearRect)
        #for cooldown:
        chargedNegBear = pygame.transform.scale(self.antiBear, (kitRect.width + self.kitNegCharge, kitRect.height + self.kitNegCharge))
        chargeNegBearRect = chargedNegBear.get_rect()
        chargeNegBearRect.center = kitRect.center
        windowSurface.blit(chargedNegBear, chargeNegBearRect)

    def moveModder(self, moveUp, moveDown):
        self.moveUp = moveUp
        self.moveDown = moveDown

    def BearMove(self):
        kitRect = self.kitRect
        laserdis = self.laserdis
        laserRect = self.laserRect
        kitMove = self.kitMove
        moveUp = self.moveUp
        moveDown = self.moveDown
        if moveUp and kitRect.top+laserdis+(laserRect.height) < WINDOWHEIGHT and True:
            kitRect.move_ip(0, kitMove)
        if moveDown and kitRect.top > -laserdis and True:
    ##            laserRect.move_ip(0, -kitMove)
            self.kitRect.move_ip(0, -kitMove)
    def splazers(self, windowSurface, planets):
        global score
        global planet
        kitCharge = self.kitCharge
        if self.laserFire == True and self.kitCharge > -20:
            kitCharge-=5
            if kitCharge >= 0:
                tempPlanets = len(planets)
                planets = self.lasers(windowSurface, planets)
                planetAddCounter = tempPlanets - len(planets)
                score += tempPlanets - len(planets)
                
                         
        if self.laserFire == False:
            if self.kitCharge < 100:
                self.kitCharge += 2
                self.kitnegCharge = 0
    def center(self):
        self.kitRect.center = (0 + (self.kitRect.right-self.kitRect.left)/2, WINDOWHEIGHT/2)
  
    def lasers(self, windowSurface, planetList):
        global planet
        kitCharge = self.kitCharge
        kitRect = self.kitRect
        laserdis = self.laserdis
        laserMod = pygame.transform.scale(self.laser, (2000,20 + kitCharge))
        laserRect = laserMod.get_rect()
        laserRect.top = kitRect.top + laserdis
        laserRect.left = kitRect.right - 25
        windowSurface.blit(laserMod, laserRect)
        for p in planetList:   
            if laserRect.colliderect(p['rect']):
                p['rect'] = p['rect'].inflate(-kitCharge/2,-kitCharge/2)
                p['size'] = p['size']-kitCharge/2
                if(p['size'] <= 0):
                    planetList.remove(p)
                else:
                    p['surface'] = pygame.transform.scale(planet, (p['size'],p['size']))
        return planetList