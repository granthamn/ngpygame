import pygame as pg
import random
import math


pg.init()
screen = pg.display.set_mode((600,600),pg.SRCALPHA)
DS = pg.Surface((100,100),pg.SRCALPHA)
DS1 = pg.Surface((100,100),pg.SRCALPHA)
DS2 = pg.Surface((100,100),pg.SRCALPHA)
DS3 = pg.Surface((100,100),pg.SRCALPHA)
DS4 = pg.Surface((100,100),pg.SRCALPHA)

WHITE=(255,255,255)
BLACK=(0,0,0)

pg.display.set_caption("Circles")
theClock = pg.time.Clock()
quitIt = False
cList = []
angle = 0
angle1 = 0
angle2 = 0
angle3 = 0
angle4 = 0
randred = random.randint(0,255)
while not quitIt:
    
    theClock.tick(100)
    DS.fill(BLACK)
    
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True

    
    if angle < 360:
        
        myRect = pg.Rect(0,0,100,100)
        
        pg.draw.rect(DS,(randred,0,0),myRect)
        pg.draw.rect(DS1,(randred,0,0),myRect)
        pg.draw.rect(DS2,(randred,0,0),myRect)
        pg.draw.rect(DS3,(randred,0,0),myRect)
        pg.draw.rect(DS4,(randred,0,0),myRect)
    #recSurf = DS.get_rect()
        blitLoc = (250,250)
        blitLoc1 = (250,100)
        blitLoc2 = (400,250)
        blitLoc3 = (250,400)
        blitLoc4 = (100,250)
        blittedRect = screen.blit(DS,blitLoc)
        blittedRect1 = screen.blit(DS,blitLoc1)
        blittedRect2 = screen.blit(DS,blitLoc2)
        blittedRect3 = screen.blit(DS,blitLoc3)
        blittedRect4 = screen.blit(DS,blitLoc4)
        screen.fill(BLACK)
        centRect = blittedRect.center
        centRect1 = blittedRect1.center
        centRect2 = blittedRect2.center
        centRect3 = blittedRect3.center
        centRect4 = blittedRect4.center
        rotSurf = pg.transform.rotate(DS,angle)
        rotSurf1 = pg.transform.rotate(DS1,angle1)
        rotSurf2 = pg.transform.rotate(DS2,angle2)
        rotSurf3 = pg.transform.rotate(DS3,angle3)
        rotSurf4 = pg.transform.rotate(DS4,angle4)
        rotRect = rotSurf.get_rect()
        rotRect1 = rotSurf1.get_rect()
        rotRect2 = rotSurf2.get_rect()
        rotRect3 = rotSurf3.get_rect()
        rotRect4 = rotSurf4.get_rect()
        rotRect.center = centRect
        rotRect1.center = centRect1
        rotRect2.center = centRect2
        rotRect3.center = centRect3
        rotRect4.center = centRect4
        
        screen.blit(rotSurf,rotRect)
        screen.blit(rotSurf1,rotRect1)
        screen.blit(rotSurf2,rotRect2)
        screen.blit(rotSurf3,rotRect3)
        screen.blit(rotSurf4,rotRect4)
        pg.display.flip()
        
        angle -= 10
        angle1 -= 5
        angle2 -= 3
        angle3 -= 1
        angle4 -= 7
        
    else:
        angle = 0
        angle1 = 0
        angle2 = 0
        angle3 = 0
        angle4 = 0
pg.quit()


