import pygame as pg
import random
import math


pg.init()
DS = pg.display.set_mode((600,600))

WHITE=(255,255,255)
BLACK=(0,0,0)
pg.display.set_caption("Circles")
theClock = pg.time.Clock()
quitIt = False
cList = []
while not quitIt:
    #DS.fill(BLACK)
    theClock.tick(50)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True

    for c in range(0,100,2):
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        pg.draw.circle(DS,(r,g,b),(100+c*3,100+c*3),100+c,1)
            
        pg.display.update()
    
pg.quit()


