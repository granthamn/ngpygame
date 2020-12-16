import pygame as pg
import random
import math


pg.init()
DS = pg.display.set_mode((500,500))
WHITE=(255,255,255)
BLACK=(0,0,0)
pg.display.set_caption("Lines n Shapes")


DS.fill(BLACK)
pg.display.update()
theClock = pg.time.Clock()

quitIt = False
while not quitIt:
    theClock.tick(60)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
    color = (random.randint(0,255),0,0)
    xEnd = random.randint(1,500)
    yEnd = random.randint(1,500)
    pg.draw.line(DS,color,(250,250),(xEnd,yEnd))
    pg.display.update()
    
quitIt = False
while not quitIt:
    DS.fill(BLACK)
    theClock.tick(60)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
    color = WHITE
    yStart = random.randint(1,500)
    pg.draw.line(DS,WHITE,(0,yStart),(500,yStart))
    pg.display.update()

quitIt = False
while not quitIt:
    DS.fill(BLACK)
    theClock.tick(60)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
    color = WHITE
    xStart = random.randint(1,500)
    pg.draw.line(DS,WHITE,(xStart,0),(xStart,500))
    pg.display.update()


quitIt = False
while not quitIt:
    #DS.fill(BLACK)
    theClock.tick(60)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
    r, g, b  = random.randint(1,255), random.randint(1,255), random.randint(1,255)
    xStart = random.randint(1,500)
    pg.draw.line(DS,(r,g,b),(xStart,0),(xStart,500))
    pg.display.update()


# TO DO - Overlapping circles at different speeds then see if we can use transparency
quitIt = False
startX = 50
startXSlower = 50
rad = 50
maxX = 450
goingRight = True
slowGoingRight = True
FPS = 30
FPSSlower = 20
startXSlower = FPS

while not quitIt:
    DS.fill(BLACK)
    theClock.tick(60)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
            if ev.key == pg.K_LEFT and FPS > 10:
                FPS -= 3
                FPSSlower -= 1
            if ev.key == pg.K_RIGHT and FPS < 60:
                FPS += 3
                FPSSlower += 1
    r, g, b  = random.randint(1,255), random.randint(1,255), random.randint(1,255)
    #print(startX)
    if startX < maxX and startX > 50:
        if goingRight:
            startX += FPS
        else:
            startX -= FPS
    elif startX >= maxX:
        goingRight = False
        startX -= FPS
    elif startX <= rad:
        goingRight = True
        startX += FPS

    if startXSlower < maxX and startXSlower > 50:
        if slowGoingRight:
            startXSlower += FPSSlower
        else:  
            startXSlower -= FPSSlower
    elif startXSlower >= maxX:
        slowGoingRight = False
        startXSlower -= FPSSlower
    elif startXSlower <= rad:
        slowGoingRight = True
        startXSlower += FPSSlower
    
 
    
    pg.draw.circle(DS,(255,0,100),(startX,rad),rad)
    pg.draw.circle(DS,(0,255,100),(int(startXSlower),rad),rad)

    pg.display.update()

pg.quit()


