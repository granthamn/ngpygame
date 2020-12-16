import pygame as pg
import random
import math


pg.init()
screen = pg.display.set_mode((600,600))
DS = pg.Surface((600,600))
WHITE=(255,255,255)
BLUE=(0,100,255)
YELLOW=(255,255,0)
BLACK=(0,0,0)
pg.display.set_caption("Stars")
theClock = pg.time.Clock()
quitIt = False
cList = []
while not quitIt:
    #DS.fill(BLACK)
    theClock.tick(100)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
                
    cx = random.randint(10,580)
    cy = random.randint(10,580)
    if len(cList) < 800:    
        cList.append((WHITE,(cx,cy),1))
        #cList.append((BLUE,(cx,cy),1))
    for c in cList:
        pg.draw.circle(DS,c[0],c[1],c[2])
        tempxy = c[1]
        cList.remove(c)
        if c[0][1] > 0:
            #c = ((c[0][0],c[0][1]-2,c[0][2]-5),tempxy,1)
            c = ((c[0][0]-1,c[0][1]-1,c[0][2]-1),tempxy,1)
            cList.append(c)
    screen.blit(DS,(0,0))        
    pg.display.flip()
    
pg.quit()


