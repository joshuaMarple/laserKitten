import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
TEXTCOLOR = (0,0,0)
BACKGROUNDCOLOR = (255,255,255)
FPS = 40
planetSize = 40
planetMoveMin = 2
planetMoveMax = 8
ADDNEWPLANETRATE = 5
planets = []
score = 0
EarthHealth = 100

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Kitten Lasers')
pygame.mouse.set_visible(False)
kittyPic = pygame.image.load('cat.png')
planet = pygame.image.load('okayplanet.png')
laser = pygame.image.load('laser.jpg')
background = pygame.image.load('space.png')
chargedKitty = pygame.image.load('catbeam.png')
antiKitty = pygame.image.load('catnegbeam.png')

font1 = pygame.font.SysFont(None, 48)

windowSurface.fill(BACKGROUNDCOLOR)
windowSurface.blit(background, (0,0))

font1 = pygame.font.SysFont(None, 48)



def terminate():
    pygame.quit()
    sys.exit()

def waitKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

class kitty:
    def __init__(self):
        self.laserdis = 50
        self.kitMove = 15
        self.laserFire = False
        self.kitCharge = 0
        self.kitNegCharge = 0
        self.laserMod = pygame.transform.scale(laser, (2000,20 + self.kitCharge))
        self.laserMod = pygame.transform.scale(laser, (2000,20 + self.kitCharge))
        self.kitRect = kittyPic.get_rect()
        self.laserRect = self.laserMod.get_rect()

    def chargeKitty(self):
        kitRect = self.kitRect
        kitCharge = self.kitCharge
        chargedCat = pygame.transform.scale(chargedKitty, (kitRect.width + kitCharge, kitRect.height + kitCharge))
        chargeCatRect = chargedCat.get_rect()
        chargeCatRect.center = kitRect.center
        windowSurface.blit(chargedCat, chargeCatRect)
        #for cooldown:
        chargedNegCat = pygame.transform.scale(antiKitty, (kitRect.width + self.kitNegCharge, kitRect.height + self.kitNegCharge))
        chargeNegCatRect = chargedNegCat.get_rect()
        chargeNegCatRect.center = kitRect.center
        windowSurface.blit(chargedNegCat, chargeNegCatRect)

    def kittyMove(self):
        kitRect = self.kitRect
        laserdis = self.laserdis
        laserRect = self.laserRect
        kitMove = self.kitMove
        if moveUp and kitRect.top+laserdis+(laserRect.height) < WINDOWHEIGHT and True:
            kitRect.move_ip(0, kitMove)
        if moveDown and kitRect.top > -laserdis and True:
    ##            laserRect.move_ip(0, -kitMove)
            self.kitRect.move_ip(0, -kitMove)
    def splazers(self, planets):
        global score
        kitCharge = self.kitCharge
        if self.laserFire == True and self.kitCharge > -20:
            kitCharge-=5
            if kitCharge >= 0:
                tempPlanets = len(planets)
                planets = kit.lasers(planets)
                planetAddCounter = tempPlanets - len(planets)
                score += tempPlanets - len(planets)
                
                         
        if self.laserFire == False:
            if self.kitCharge < 100:
                self.kitCharge += 2
                self.kitnegCharge = 0
    def center(self):
        self.kitRect.center = (0 + (self.kitRect.right-self.kitRect.left)/2, WINDOWHEIGHT/2)
  
    def lasers(self, planetList):
        kitCharge = self.kitCharge
        kitRect = self.kitRect
        laserdis = self.laserdis
        laserMod = pygame.transform.scale(laser, (2000,20 + kitCharge))
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

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def earthDead():
    global EarthHealth
    drawText('EARTH IS DESTROYED!', font1, windowSurface, (WINDOWWIDTH /8), (WINDOWHEIGHT / 3))
    drawText('YOU HAVE FAILED US, LASERKITTEN.', font1, windowSurface, (WINDOWWIDTH /8), (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(background, (0,0))
    drawText('Press N for a new game', font1, windowSurface, (WINDOWWIDTH /8), (WINDOWHEIGHT / 3))
    drawText('Maybe you won\'t suck so hard this time', font1, windowSurface, (WINDOWWIDTH /8), (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitKey()
    for i in planets[:]:
        planets.remove(i)
    EarthHealth = 100
    planetAddCounter = 5
    kitCharge = 0
    score = 0

def genPlanets(planetList):
    randomPlanet = random.random() + (score/1000.)
    if randomPlanet >= .97:
        planetSize = random.randint(20, 200)+score/100
        newPlanet = {'size':planetSize,
                    'rect': pygame.Rect(WINDOWWIDTH - planetSize
                                         , random.randint(0, WINDOWHEIGHT-planetSize+score/10), planetSize, planetSize),
                     'speed': random.randint(planetMoveMin, planetMoveMax+score/100),
                     'surface':pygame.transform.scale(planet, (planetSize, planetSize)), }

        planetList.append(newPlanet)
    return planetList



def planetChecker():
    global EarthHealth
    for p in planets:
        p['rect'].move_ip(-p['speed'], random.randint(-5,5))

    for p in planets[:]:
        if p['rect'].left < 0:
            planets.remove(p)
            EarthHealth -= p['size']/10

def redraw(kit, planets):
    global window
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(background, (0,0))
    
    #draw text
    drawText('Score: %s' % (score), font1, windowSurface, 10, 0)
    drawText('Earth Health: %s' % (EarthHealth), font1, windowSurface, 10, 48)
    for p in planets:
        windowSurface.blit(p['surface'], p['rect'])
        
    kit.chargeKitty()
    windowSurface.blit(kittyPic, kit.kitRect)
    kit.splazers(planets)
    pygame.display.update()


    mainClock.tick(FPS)

def earthChecker():
    global EarthHealth
    if EarthHealth <= 0:
        EarthHealth = 100
        earthDead()

# kitRect = kitty.get_rect()
# laserRect = laserMod.get_rect()
windowSurface.fill(BACKGROUNDCOLOR)
windowSurface.blit(background, (0,0))

drawText('KITTEN LASERS!', font1, windowSurface, (WINDOWWIDTH /3), (WINDOWHEIGHT / 3))
drawText("Protector of Earth. LaserCat has made it his sworn", font1, windowSurface, (WINDOWWIDTH/8), (WINDOWHEIGHT / 3) + 50)
drawText("duty to protect all Earthlings from the evil planets.", font1, windowSurface, (WINDOWWIDTH/8), (WINDOWHEIGHT / 3)+ 100)
drawText("PRESS ANY KEY TO BEGIN THE DEFENSE.", font1, windowSurface, (WINDOWWIDTH/8), (WINDOWHEIGHT / 3)+150)
pygame.display.update()
waitKey()
kit = kitty()
while True:

    kit.center()
    
    moveLeft = moveRight = moveUp = moveDown = False
    planetAddCounter = 5

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    moveUp = True
                    moveDown = False
                if event.key == K_UP:
                    moveDown = True
                    moveUp = False
                if event.key == K_SPACE:
                    kit.laserFire = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    drawText('press any key to unpause', font1, windowSurface, (WINDOWWIDTH /3), (WINDOWHEIGHT / 3))
                    drawText('press esc again to exit', font1, windowSurface, (WINDOWWIDTH /3), (WINDOWHEIGHT / 3) + 50)
                    pygame.display.update()
                    waitKey()
                if event.key == K_UP:
                    moveDown = False
                    moveUp = False
                if event.key == K_DOWN:
                    moveUp = False
                    moveDown = False
                if event.key == K_SPACE:
                    kit.laserFire = False

        planets = genPlanets(planets)


        
        kit.kittyMove()

        planetChecker()

        earthChecker()
        
       

        redraw(kit, planets)
        
