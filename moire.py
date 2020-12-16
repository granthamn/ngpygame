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

        


    def draw(self,time):
       
    
        for y in range(SCREEN_HEIGHT):
          
            for x in range(SCREEN_WIDTH):
                shade1 = 128+127 * (math.sin(math.hypot(400-y,400-x)/16))
                
                #self.DS.set_at((x,y),(shade,shade,shade))
                self.moireArray[x,y,:] = (shade1,shade1,shade1)
        
        surfarray.blit_array(self.DS,self.moireArray)
                
                
    def main(self):

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
