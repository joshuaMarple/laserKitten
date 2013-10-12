import pygame, sys, random
from pygame.locals import *
# from pygame.sprite import *
from rocket import *
import globalDefs
class Corgi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.image = pygame.transform.scale(pygame.image.load('./res/corgi.jpeg'), (40,40))
        self.rect = self.image.get_rect()
        self.rocketInc = 0
        # self.rocketImg = pygame.image.load('./res/rocket.png')
        # self.rocketSpeed = 5
        # self.corgiMove = 15
        # self.rocket = pygame.transform.scale(self.rocketImg, (20,20))
        # self.corgiPic = pygame.transform.scale(self.corgiPic, (70,70))
        # self.corgiRect = self.corgiPic.get_rect()
        # self.laserRect = self.laser.get_rect()
        # self.moveUp = False
        # self.moveDown = False
        # self.health = 100
        self.rockets = pygame.sprite.Group()

    def fireRockets(self):
        newrocket = rocket()
        # newrocket.image = pygame.transform.scale(pygame.image.load('./res/rocket.png'), (40,40))
        # rocket.rect = rocket.image.get_rect()
        newrocket.rect.top = self.rect.bottom
        self.rockets.add(newrocket)

    def update(self, rect, windowSurface):
        self.rocketInc += 1
        if (self.rocketInc >= 25):
            self.fireRockets()
            self.rocketInc = 0
        self.rockets.update()
        self.rockets.draw(windowSurface)
        # self.pygame.sprite.draw(windowSurface)
        # print(self.rockets)
        self.corgiMove(rect)
        if (self.health < 0):
            return "dead"

    def corgiMove(self, kitrect):
        self.rect.top = kitrect.bottom
        self.rect.right = kitrect.right
        # self.rect.move(kitrect.right, kit rect.bottom)

    def splazers(self, windowSurface, planets):
        if self.laserFire == True and self.corgiCharge > -20:
            self.corgiCharge-=5
            if self.corgiCharge >= 0:
                tempPlanets = len(planets)
                planets = self.lasers(windowSurface, planets)
                planetAddCounter = tempPlanets - len(planets)
                globalDefs.score += tempPlanets - len(planets)
                
                         
        if self.laserFire == False:
            if self.corgiCharge < 100:
                self.corgiCharge += 2
                self.corginegCharge = 0
    def center(self):
        self.corgiRect.center = (0 + (self.corgiRect.right-self.corgiRect.left)/2, globalDefs.WINDOWHEIGHT/2)
  
    def lasers(self, windowSurface, planetList):
        self.laser = pygame.transform.scale(self.laserImg, (2000, self.corgiCharge))
        self.laserRect.height = self.corgiCharge
        self.laserRect.top = int(self.corgiRect.y)
        self.laserRect.left = self.corgiRect.right
        windowSurface.blit(self.laser, self.laserRect)
        for p in planetList:   
            if self.laserRect.colliderect(p['rect']):
                p['rect'] = p['rect'].inflate(-self.corgiCharge/3,-self.corgiCharge/3)
                p['size'] = p['size']-self.corgiCharge/3
                if(p['size'] <= 0):
                    planetList.remove(p)
                else:
                    p['surface'] = pygame.transform.scale(globalDefs.planet, (p['size'],p['size']))
        return planetList