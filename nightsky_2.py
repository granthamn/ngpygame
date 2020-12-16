import pygame as pg
import random
import math


pg.init()
screen = pg.display.set_mode((600,600))
DS = pg.Surface((600,600))
WHITE=(255,255,255)
YELLOW=(255,255,0)
BLACK=(0,0,0)
pg.display.set_caption("Stars")
theClock = pg.time.Clock()
quitIt = False
cList = []
while not quitIt:
    DS.fill(BLACK)
    theClock.tick(500)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
                
    cx = random.randint(4,595)
    cy = random.randint(4,595)
    if len(cList) < 200:    
        #cList.append((WHITE,(cx,cy),1))
        cList.append((WHITE,(cx,cy),1))
    for c in cList:
        pg.draw.circle(DS,c[0],c[1],c[2])
        # see if we can move these stars as they fade
        tempxy = (c[1][0],c[1][1]+1)
        cList.remove(c)
        if c[0][0] > 5:
            c = ((c[0][0]-1,c[0][1]-1,c[0][2]-1),tempxy,1)
            #c = ((c[0][0]-5,c[0][1]-5,c[0][2]),tempxy,1)
            cList.append(c)

    screen.blit(DS,(0,0))
    pg.display.flip()
pg.quit()


