import pygame as pg
import random
import math
from enum import Enum


pg.init()
pg.font.init()
screen = pg.display.set_mode((600,600))
DS = pg.Surface((600,600))

class FONTYDIR(Enum):
    FONTYUP = 0
    FONTYDOWN = 1

WHITE=(255,255,255)
BLACK=(0,0,0)
pg.display.set_caption("Letters")
theClock = pg.time.Clock()
quitIt = False
fontyDict = {}
fontyList = []
maxFonty = 128
minFonty = 8
fontyStep = 4
#Preload fonts
for i in range(4,132,4):
    font = pg.font.SysFont("Comic Sans",i)
    fontyDict[i] = font

while not quitIt:
    DS.fill(BLACK)
    theClock.tick(100)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
            else:
                text = pg.key.name(ev.key)
                

                r = random.randint(1,255)
                g = random.randint(1,255)
                b = random.randint(1,255)
                x = random.randint(20,550)
                y = random.randint(20,550)
                randySize = random.randrange(4,128,4)
                if randySize < maxFonty:
                    fontyDir = FONTYDIR.FONTYDOWN
                else:
                    fontyDir = FONTYDIR.FONTYUP
                fontyList.append([(x,y),(r,g,b),randySize,fontyDir,text])
    for fonty in fontyList:
        lett = fontyDict[fonty[2]].render(fonty[4],True,fonty[1])
        DS.blit(lett,fonty[0])
        # Increase fonty size
        if fonty[2] < maxFonty and fonty[2] > minFonty:
            if fonty[3] == FONTYDIR.FONTYUP:
                fonty[2] += fontyStep
            else:
                fonty[2] -= fontyStep
        elif fonty[2] == maxFonty:
            fonty[3] = FONTYDIR.FONTYDOWN
            fonty[2] -= fontyStep
        else:
            fonty[3] = FONTYDIR.FONTYUP
            fonty[2] += fontyStep
                
        
    screen.blit(DS,(0,0))    
    pg.display.flip()
    
pg.quit()


