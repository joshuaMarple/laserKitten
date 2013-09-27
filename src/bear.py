import pygame, sys, random
from pygame.locals import *
import globalDefs
class bear:
    def __init__(self):
        self.BearPic = pygame.image.load('./res/spacebear.jpg')
        self.laser = pygame.image.load('./res/laserTest.png')
        self.chargedBear = pygame.image.load('./res/catbeam.png')
        self.antiBear = pygame.image.load('./res/catnegbeam.png')
        self.laserdis = 50
        self.bearMove = 15
        self.laserFire = False
        self.bearCharge = 0
        self.bearNegCharge = 0
        self.laserMod = pygame.transform.scale(self.laser, (2000,20 + self.bearCharge))
        self.laserMod = pygame.transform.scale(self.laser, (2000,20 + self.bearCharge))
        self.BearPic = pygame.transform.scale(self.BearPic, (50,50))
        self.bearRect = self.BearPic.get_rect()
        self.laserRect = self.laserMod.get_rect()
        self.moveUp = False
        self.moveDown = False

    def chargeBear(self, windowSurface):
        bearRect = self.bearRect
        bearCharge = self.bearCharge
        chargedBear = pygame.transform.scale(self.chargedBear, (bearRect.width + bearCharge, bearRect.height + bearCharge))
        chargeBearRect = chargedBear.get_rect()
        chargeBearRect.center = bearRect.center
        # windowSurface.blit(chargedBear, chargeBearRect)
        #for cooldown:
        chargedNegBear = pygame.transform.scale(self.antiBear, (bearRect.width + self.bearNegCharge, bearRect.height + self.bearNegCharge))
        chargeNegBearRect = chargedNegBear.get_rect()
        chargeNegBearRect.center = bearRect.center
        # windowSurface.blit(chargedNegBear, chargeNegBearRect)

    def moveModder(self, moveUp, moveDown):
        self.moveUp = moveUp
        self.moveDown = moveDown

    def BearMove(self):
        mover = random.random()
        if (mover > 0.9):
            self.moveUp = True
        elif (mover > 0.8):
            self.moveDown = True
        elif (mover > 0.75):
            self.moveUp = False
        elif (mover > 0.7):
            self.moveDown = False
        if self.moveUp and self.bearRect.top+self.laserdis+(self.laserRect.height) < globalDefs.WINDOWHEIGHT:
            self.bearRect.move_ip(0, self.bearMove)
        if self.moveDown and self.bearRect.top > -self.laserdis:
            self.bearRect.move_ip(0, -self.bearMove)
    def splazers(self, windowSurface, planets):
        splaser = random.random()
        if(splaser > 0.8):
            self.laserFire = True
        elif(splaser > 0.4):
            self.laserFire = False
        if self.laserFire == True and self.bearCharge > -20:
            self.bearCharge-=3
            if self.bearCharge >= 0:
                tempPlanets = len(planets)
                planets = self.lasers(windowSurface, planets)
                planetAddCounter = tempPlanets - len(planets)
                globalDefs.score += tempPlanets - len(planets)
                
                         
        if self.laserFire == False:
            if self.bearCharge < 150:
                self.bearCharge += 2
                self.bearnegCharge = 0
    def center(self):
        self.bearRect.center = (globalDefs.WINDOWWIDTH - (self.bearRect.right-self.bearRect.left)/2, globalDefs.WINDOWHEIGHT/2)
  
    def lasers(self, windowSurface, planetList):
        global planet
        bearCharge = self.bearCharge
        bearRect = self.bearRect
        laserdis = self.laserdis
        laserMod = pygame.transform.scale(self.laser, (2000,20 + bearCharge))
        laserRect = laserMod.get_rect()
        laserRect.top = bearRect.top + laserdis
        laserRect.right = bearRect.left + 25
        windowSurface.blit(laserMod, laserRect)
        for p in planetList:   
            if laserRect.colliderect(p['rect']):
                p['rect'] = p['rect'].inflate(-bearCharge/2,-bearCharge/2)
                p['size'] = p['size']-bearCharge/2
                if(p['size'] <= 0):
                    planetList.remove(p)
                else:
                    p['surface'] = pygame.transform.scale(globalDefs.planet, (p['size'],p['size']))
        return planetList
