def lasers(WINDOWWIDTH, planet, kitRect):
    laser = pygame.image.load('laser.jpg')
    laserMod = pygame.transform.scale(laser, (200,20))
    laserRect = laser.get_rect()
##    laserRect.top = kitRect.top
##    laserRect.left = kitRect.right
    windowSurface.blit(laserMod, laserRect)
    if planet.colliderect(laserRect):
        return true
    for p in planets:
        if laserRect.colliderect(p['rect']):
            planets.remove(p)
    
    return false
