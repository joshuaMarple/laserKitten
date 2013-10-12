import pygame, sys, random
from pygame.locals import *
import globalDefs
class kitty:
    def __init__(self):
        self.kittyPic = pygame.image.load('./res/cat.png')
        self.laserImg = pygame.image.load('./res/laser.png')
        self.chargedKitty = pygame.image.load('./res/catbeam.png')
        self.antiKitty = pygame.image.load('./res/catnegbeam.png')
        self.laserdis = 0
        self.kitMove = 25
        self.laserFire = False
        self.kitCharge = 0
        self.kitNegCharge = 0
        self.laser = pygame.transform.scale(self.laserImg, (2000,20 + self.kitCharge))
        # self.laserMod = pygame.transform.scale(self.laser, (2000,20 + self.kitCharge))
        self.kittyPic = pygame.transform.scale(self.kittyPic, (70,70))
        self.kitRect = self.kittyPic.get_rect()
        self.laserRect = self.laser.get_rect()
        self.moveUp = False
        self.moveDown = False
        self.health = 100

    def chargeKitty(self, windowSurface):
        chargedCat = pygame.transform.scale(self.chargedKitty, (self.kitRect.width + self.kitCharge, self.kitRect.height + self.kitCharge))
        chargeCatRect = chargedCat.get_rect()
        chargeCatRect.center = self.kitRect.center
        windowSurface.blit(chargedCat, chargeCatRect)
        #for cooldown:
        chargedNegCat = pygame.transform.scale(self.antiKitty, (self.kitRect.width + self.kitNegCharge, self.kitRect.height + self.kitNegCharge))
        chargeNegCatRect = chargedNegCat.get_rect()
        chargeNegCatRect.center = self.kitRect.center
        windowSurface.blit(chargedNegCat, chargeNegCatRect)

    def moveModder(self, moveUp, moveDown):
        self.moveUp = moveUp
        self.moveDown = moveDown

    def update(self):
        self.kittyMove()
        if (self.health < 0):
            return "dead"

    def kittyMove(self):
        if self.moveUp and self.kitRect.top+self.laserdis+(self.laserRect.height) < globalDefs.WINDOWHEIGHT:
            self.kitRect.move_ip(0, self.kitMove)
        if self.moveDown and self.kitRect.top > -self.laserdis:
    ##            laserRect.move_ip(0, -kitMove)
            self.kitRect.move_ip(0, -self.kitMove)
    def splazers(self, windowSurface, planets):
        if self.laserFire == True and self.kitCharge > -20:
            self.kitCharge-=5
            if self.kitCharge >= 0:
                tempPlanets = len(planets)
                planets = self.lasers(windowSurface, planets)
                planetAddCounter = tempPlanets - len(planets)
                globalDefs.score += tempPlanets - len(planets)
                
                         
        if self.laserFire == False:
            if self.kitCharge < 100:
                self.kitCharge += 2
                self.kitnegCharge = 0
    def center(self):
        self.kitRect.center = (0 + (self.kitRect.right-self.kitRect.left)/2, globalDefs.WINDOWHEIGHT/2)
  
    def lasers(self, windowSurface, planetList):
        self.laser = pygame.transform.scale(self.laserImg, (2000, self.kitCharge))
        self.laserRect.height = self.kitCharge
        self.laserRect.top = int(self.kitRect.y)
        self.laserRect.left = self.kitRect.right
        windowSurface.blit(self.laser, self.laserRect)
        for p in planetList:   
            if self.laserRect.colliderect(p['rect']):
                p['rect'] = p['rect'].inflate(-self.kitCharge/3,-self.kitCharge/3)
                p['size'] = p['size']-self.kitCharge/3
                if(p['size'] <= 0):
                    planetList.remove(p)
                else:
                    p['surface'] = pygame.transform.scale(globalDefs.planet, (p['size'],p['size']))
        return planetList