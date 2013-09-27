import pygame, random, sys
from pygame.locals import *
import globalDefs
from kitty import *
from bear import *
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((globalDefs.WINDOWWIDTH, globalDefs.WINDOWHEIGHT))
pygame.display.set_caption('Kitten Lasers')
pygame.mouse.set_visible(False)
windowSurface.fill(globalDefs.BACKGROUNDCOLOR)
windowSurface.blit(globalDefs.background, (0,0))
font1 = pygame.font.SysFont(None, 48)
# font1 = pygame.font.SysFont(None, 48)

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
                if event.key == K_RETURN:
                    return

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, globalDefs.TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def earthDead():
    drawText('EARTH IS DESTROYED!', font1, windowSurface, (globalDefs.WINDOWWIDTH /8), (globalDefs.WINDOWHEIGHT / 3))
    drawText('YOU HAVE FAILED US, LASERKITTEN.', font1, windowSurface, (globalDefs.WINDOWWIDTH /8), (globalDefs.WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitKey()
    windowSurface.fill(globalDefs.BACKGROUNDCOLOR)
    windowSurface.blit(globalDefs.background, (0,0))
    drawText('Press Enter for a new game', font1, windowSurface, (globalDefs.WINDOWWIDTH /8), (globalDefs.WINDOWHEIGHT / 3))
    drawText('Maybe you won\'t suck so hard this time', font1, windowSurface, (globalDefs.WINDOWWIDTH /8), (globalDefs.WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitKey()
    for i in globalDefs.planets[:]:
        globalDefs.planets.remove(i)
    globalDefs.EarthHealth = 100
    planetAddCounter = 5
    kitCharge = 0
    globalDefs.score = 0

def genPlanets(planetList):
    randomPlanet = random.random()
    if randomPlanet >= (.98 - (globalDefs.score/1000.)):
        planetSize = random.randint(20, 200)+globalDefs.score/100
        newPlanet = {'size':planetSize,
                    'rect': pygame.Rect(globalDefs.WINDOWWIDTH - planetSize
                                         , random.randint(0, globalDefs.WINDOWHEIGHT-planetSize+globalDefs.score/10), planetSize, planetSize),
                     'speed': random.randint(globalDefs.planetMoveMin, globalDefs.planetMoveMax+globalDefs.score/100),
                     'surface':pygame.transform.scale(globalDefs.planet, (planetSize, planetSize)), }

        planetList.append(newPlanet)
    return planetList



def planetChecker():
    for p in globalDefs.planets:
        p['rect'].move_ip(-p['speed'], random.randint(-5,5))

    for p in globalDefs.planets[:]:
        if p['rect'].left < 0:
            globalDefs.planets.remove(p)
            globalDefs.EarthHealth -= p['size']/10

def redraw(kit, bear, planets):
    global window
    windowSurface.fill(globalDefs.BACKGROUNDCOLOR)
    windowSurface.blit(globalDefs.background, (0,0))
    
    #draw text
    drawText('Score: %s' % (globalDefs.score), font1, windowSurface, 10, 0)
    drawText('Earth Health: %s' % (globalDefs.EarthHealth), font1, windowSurface, 10, 48)
    for p in globalDefs.planets:
        windowSurface.blit(p['surface'], p['rect'])
        
    kit.chargeKitty(windowSurface)
    beary.chargeBear(windowSurface)
    windowSurface.blit(kit.kittyPic, kit.kitRect)
    windowSurface.blit(beary.BearPic, beary.bearRect)

    kit.splazers(windowSurface, planets)
    beary.splazers(windowSurface, planets)
    pygame.display.update()

    earthHealthIncrementer()
    mainClock.tick(globalDefs.FPS)

def earthHealthIncrementer():
    globalDefs.earthHealthCounter +=1
    if (globalDefs.earthHealthCounter > 100 & globalDefs.EarthHealth < 100):
        globalDefs.EarthHealth += 1
        globalDefs.earthHealthCounter = 0

def earthChecker():
    if globalDefs.EarthHealth <= 0:
        globalDefs.EarthHealth = 100
        earthDead()

def eventChecker(event, kit):
    if event.type == QUIT:
        terminate()
    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            kit.moveModder(True, False)
            beary.moveModder(True, False)
        if event.key == K_UP:
            kit.moveModder(False, True)
            beary.moveModder(False, True)
        if event.key == K_SPACE:
            kit.laserFire = True
    if event.type == KEYUP:
        if event.key == K_ESCAPE:
            drawText('press enter to unpause', font1, windowSurface, (globalDefs.WINDOWWIDTH /3), (globalDefs.WINDOWHEIGHT / 3))
            drawText('press esc again to exit', font1, windowSurface, (globalDefs.WINDOWWIDTH /3), (globalDefs.WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitKey()
        if event.key == K_UP:
            kit.moveModder(False, False)
            beary.moveModder(False, False)
        if event.key == K_DOWN:
            kit.moveModder(False, False)
            beary.moveModder(False, False)
        if event.key == K_SPACE:
            kit.laserFire = False

windowSurface.fill(globalDefs.BACKGROUNDCOLOR)
windowSurface.blit(globalDefs.background, (0,0))

drawText('KITTEN LASERS!', font1, windowSurface, (globalDefs.WINDOWWIDTH /3), (globalDefs.WINDOWHEIGHT / 3))
drawText("Protector of Earth. LaserCat has made it his sworn", font1, windowSurface, (globalDefs.WINDOWWIDTH/8), (globalDefs.WINDOWHEIGHT / 3) + 50)
drawText("duty to protect all Earthlings from the evil planets.", font1, windowSurface, (globalDefs.WINDOWWIDTH/8), (globalDefs.WINDOWHEIGHT / 3)+ 100)
drawText("PRESS ENTER TO BEGIN THE DEFENSE.", font1, windowSurface, (globalDefs.WINDOWWIDTH/8), (globalDefs.WINDOWHEIGHT / 3)+150)
pygame.display.update()
waitKey()
kit = kitty()
kit.center()
beary = bear()
beary.center()
while True:
    for event in pygame.event.get():
        eventChecker(event, kit)

    globalDefs.planets = genPlanets(globalDefs.planets)
    
    kit.kittyMove()

    beary.BearMove()

    planetChecker()

    earthChecker()

    # scoreChecker()

    redraw(kit, beary, globalDefs.planets)
    
