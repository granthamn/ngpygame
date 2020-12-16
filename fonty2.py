import pygame as pg
import random
import math


pg.init()
pg.font.init()
DS = pg.display.set_mode((600,600))
fontySize = 48
fonty = pg.font.SysFont("Comic Sans",fontySize)
WHITE=(255,255,255)
BLACK=(0,0,0)
pg.display.set_caption("Letters")
theClock = pg.time.Clock()
quitIt = False

while not quitIt:
    #DS.fill(BLACK)
    theClock.tick(50)
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
            elif ev.key == pg.K_UP:
                fontySize += 4
                fonty = pg.font.SysFont("Comic Sans",fontySize)
            elif ev.key == pg.K_DOWN:
                fontySize -= 4
                fonty = pg.font.SysFont("Comic Sans",fontySize)
            else:
                text = pg.key.name(ev.key)

                r = random.randint(1,255)
                g = random.randint(1,255)
                b = random.randint(1,255)
                x = random.randint(20,550)
                y = random.randint(20,550)
                lett = fonty.render(text,True,(r,g,b))
                
                DS.blit(lett,(x,y))
            
    pg.display.update()
    
pg.quit()


