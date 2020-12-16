import pygame as pg
import random
import math


pg.init()
DS = pg.display.set_mode((500,500))

pg.display.set_caption("Lines")


DS.fill((0,0,0))
pg.display.update()
theClock = pg.time.Clock()

quitIt = False
while not quitIt:
    theClock.tick()
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
    for i in range(0,500):
        for j in range(1,70):
            color = (random.randint(0,255),0,0)
            xEnd = random.randint(1,300)
            yEnd = random.randint(1,300)
            pg.draw.line(DS,color,(i,0),(xEnd,yEnd))
            pg.display.update()
        DS.fill((0,0,0))

    for i in range(0,500):
        for j in range(1,70):
            color = (random.randint(0,255),0,0)
            xEnd = random.randint(1,300)
            yEnd = random.randint(1,300)
            pg.draw.line(DS,color,(500,i),(xEnd,yEnd))
            pg.display.update()
        DS.fill((0,0,0))

    for i in range(0,500):
        for j in range(1,70):
            color = (random.randint(0,255),0,0)
            xEnd = random.randint(1,300)
            yEnd = random.randint(1,300)
            pg.draw.line(DS,color,(500-i,500),(xEnd,yEnd))
            pg.display.update()
        DS.fill((0,0,0))

    for i in range(0,500):
        for j in range(1,70):
            color = (random.randint(0,255),0,0)
            xEnd = random.randint(1,300)
            yEnd = random.randint(1,300)
            pg.draw.line(DS,color,(0,500-i),(xEnd,yEnd))
            pg.display.update()
        DS.fill((0,0,0))

pg.quit()
