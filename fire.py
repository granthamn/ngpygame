import pygame as pg
import math
import time
import random
import numpy

SCREEN_WIDTH=400
SCREEN_HEIGHT=400
WINSIZE=(SCREEN_WIDTH,SCREEN_HEIGHT)

class fire:
    def __init__(self,caption):
        self.quit = False
        self.screen = pg.display.set_mode(WINSIZE)
        self.DS = pg.Surface(WINSIZE)
        pg.display.set_caption(caption)
        #self.moireArr = pg.PixelArray(self.DS)
        self.clock = pg.time.Clock()

        


    def draw(self,time):
        ttime = time * 1000
        cx1 = math.sin(ttime/2) * SCREEN_WIDTH / 3 + SCREEN_WIDTH / 2
        cy1 = math.sin(ttime/4) * SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 2
        cx2 = math.cos(ttime/3) * SCREEN_WIDTH / 3 + SCREEN_WIDTH / 2
        cy2 = math.cos(ttime) * SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 2

        for y in range(SCREEN_HEIGHT):
            dy = (y - cy1) * (y -cy1)
            dy2 = (y - cy2) * (y - cy2)
            for x in range(SCREEN_WIDTH):
                dx = (x - cx1) * (x - cx1)
                dx2 = (x - cx2) * (x - cx2)
                shade = (((int(math.sqrt(dx + dy)) ^ int(math.sqrt(dx2 + dy2))) >> 4) & 1) * 255
                self.DS.set_at((x,y),(shade,shade,shade))
                
                
    def main(self):

        #self.clock.tick()
        self.timer = time.monotonic()
        while not self.quit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True
            #theTime = self.clock.tick()
            theTimer = time.monotonic()
            theTime = theTimer - self.timer
            self.timer = theTimer
            #self.DS.fill((0,0,0))
            self.draw(theTime)
            self.screen.blit(self.DS,(0,0))
            pg.display.flip()
            
pg.init()
theFire = fire("Fire")
theFire.main()
pg.quit()
