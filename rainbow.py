import pygame as pg
import random
import math


pg.init()
DS = pg.display.set_mode((800,600))
WHITE=(255,255,255)
BLACK=(0,0,0)
pg.display.set_caption("Rainbow")

theClock = pg.time.Clock()

quitIt = False

ytop = 0
ybot = 700
radx = 400
while not quitIt:
    #DS.fill(BLACK)
    popy = 0
    theClock.tick(30)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        popy = 10
    if keys[pg.K_DOWN]:
        popy = -10
    if keys[pg.K_LEFT]:
        radx -= 10
    if keys[pg.K_RIGHT]:
        radx += 10
    ybot -= popy
    ytop += popy                
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ranwid = random.randint(3,10)
    ranrad = random.randint(100,400)
    pg.draw.circle(DS,(r,g,b),(radx,ytop),ranrad,ranwid)
    pg.draw.circle(DS,(r,g,b),(radx,ybot),ranrad,ranwid)

    pg.display.update()

pg.quit()


