import pygame, sys, random
from pygame.locals import *
import globalDefs
class rocket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.image = pygame.transform.scale(pygame.image.load('./res/rocket.png'), (40,40))
        self.rect = self.image.get_rect()

    def update(self):
        # print "i've been updated"
        self.rect.right += 5
        if(self.rect.right > globalDefs.WINDOWWIDTH):
            self.kill()
        # self.draw(surface)