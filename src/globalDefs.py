import pygame, sys
from pygame.locals import *
WINDOWWIDTH = 1200
WINDOWHEIGHT = 600
TEXTCOLOR = (0,0,0)
BACKGROUNDCOLOR = (255,255,255)
FPS = 40
planetSize = 30
planetMoveMin = 2
planetMoveMax = 8
ADDNEWPLANETRATE = 5
planets = []
score = 0
EarthHealth = 100
moveLeft = moveRight = moveUp = moveDown = False
planetAddCounter = 5
planet = pygame.image.load('./res/okayplanet.png')
background = pygame.transform.scale(pygame.image.load('./res/space.png'), (WINDOWWIDTH, WINDOWHEIGHT))
earthHealthCounter = 0