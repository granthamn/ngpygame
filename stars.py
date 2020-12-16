import pygame as pg
import math
import time
import random
import numpy as npy
import pygame.surfarray as surfarray

from numpy import int32

SCREEN_WIDTH=400
SCREEN_HEIGHT=400
WINSIZE=(SCREEN_WIDTH,SCREEN_HEIGHT)

class fire:
    def __init__(self,caption):
        self.quit = False
        self.DS = pg.display.set_mode(WINSIZE)
        self.moireArray = npy.zeros((SCREEN_WIDTH,SCREEN_HEIGHT, 3), int32)
        self.moireArray[:] = (255,0,0)
        self.moireArray[:,::3] = (0,255,255)
        pg.display.set_caption(caption)
        #self.moireArr = pg.PixelArray(self.DS)
        self.clock = pg.time.Clock()

        
    def setup(self):
        self.mArr1 = npy.zeros((SCREEN_WIDTH*2,SCREEN_HEIGHT*2),float)
        self.mArr2 = npy.zeros((SCREEN_WIDTH*2,SCREEN_HEIGHT*2),float)
        
        for i in range(SCREEN_HEIGHT * 2):
            for j in range(SCREEN_WIDTH * 2):
                self.mArr1[j,i] = 128+127 * (math.sin(math.hypot(400-i,400-j)/16))
                self.mArr2[j,i] = 128+127 * math.sin(i/(37+15*math.cos(j/74))) * math.cos(j/(31+11*math.sin(i/57)))
    def draw(self,time):
       
    
        for y in range(SCREEN_HEIGHT):
          
            for x in range(SCREEN_WIDTH):
                shade1 = 128+127 * (math.sin(math.hypot(400-y,400-x)/16))
                
                #self.DS.set_at((x,y),(shade,shade,shade))
                self.moireArray[x,y,:] = (shade1,shade1,shade1)
        
        surfarray.blit_array(self.DS,self.moireArray)
        for y in range(SCREEN_HEIGHT):
            for x in range(SCREEN_WIDTH):
                if x == 0:
                    self.moireArray[SCREEN_WIDTH-1,y,:] = self.moireArray[x,y,:]
                else:
                    self.moireArray[x-1,y,:] = self.moireArray[x,y,:]
                
    def main(self):
        self.setup()
        #self.clock.tick()
       # self.timer = time.monotonic()
        while not self.quit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True
            #theTime = self.clock.tick()
            #theTimer = time.monotonic()
            #elapsed = theTimer - self.timer
            #self.timer = theTimer
            theTime = self.clock.tick()
            #self.DS.fill((0,0,0))
            self.draw(theTime)
            pg.display.update()
            
pg.init()
theFire = fire("Fire")
theFire.main()
pg.quit()
