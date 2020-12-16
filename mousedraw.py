import pygame as pg
import random
import math

pg.Surface.get_view
pg.init()
screen = pg.display.set_mode((400,400))
DS = pg.Surface(screen.get_size())
WHITE=(255,255,255) # Constant for WHITE colour (r,g,b)
BLACK=(0,0,0)
pg.display.set_caption("Draw")
bg = BLACK
fg = WHITE
theClock = pg.time.Clock()
quitIt = False


while not quitIt:
    #DS.fill(BLACK)
    #theClock.tick()
    for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_ESCAPE:
                quitIt = True
            if ev.key == pg.K_b:
                bg = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                pg.draw.line(DS,bg,(0,0),(400,0),6)
            if ev.key == pg.K_f:
                fg = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                pg.draw.line(DS,fg,(0,400),(400,400),6)
            if ev.key == pg.K_y:
                DS.fill(bg)

    mTup = pg.mouse.get_pressed()
    if mTup[0] == 1:
        mPos = pg.mouse.get_pos()
        DS.set_at((mPos[0],mPos[1]),fg)
    screen.blit(DS,(0,0))
    pg.display.flip()

pg.quit()


