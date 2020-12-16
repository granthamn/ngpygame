import pygame as pg
import random
from seedconsts import *


class Seeds:
    def __init__(self,caption):
        self.screen  = pg.display.set_mode(WINSIZE)
        self.DS = pg.Surface(WINSIZE)
        self.clock = pg.time.Clock()
        pg.display.set_caption(caption)
        self.quit = False

        

        # 2 Buffers - display and calc
        # Uncomment next line for a Randomised starting state
        #self.calcBuff = [[random.randint(0,1) for x in range(PLAY_WIDTH)] for y in range (PLAY_HEIGHT)]
        # Uncomment next line for a blank starting point followed by a set pattern
        self.calcBuff = [[0 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]   

        # Randomise a 10 * 10 grid of either alive or dying cells
        for y in range(10):
            for x in range(10):
                self.calcBuff[55+y][85+x] = random.randint(0,1)
        

        
    def deadOrAlive(self,py,px):
        # There are 3 states - Dead = 0, Dying = 1, Alive = 2
        # Rules:
        # A dead cell becomes alive if it has exactly two alive neighbours.
        # Alive cells become dying
        # Dying cells become dead
        state = 0
        # Count alive neighbours
        neighbours = self.dispBuff[py-1][px-1] + self.dispBuff[py-1][px] + self.dispBuff[py-1][px+1]  \
                   + self.dispBuff[py][px-1]   + 0                       + self.dispBuff[py][px+1]    \
                   + self.dispBuff[py+1][px-1] + self.dispBuff[py+1][px] + self.dispBuff[py+1][px+1]

        if self.dispBuff[py][px] == 0 and neighbours == 2:
            #It's a miracle!
            state = 1
        else:
            state = 0
            
        return state
        
    def mainLoop(self):
        space = 0
        while not self.quit:
            #Timings - 20fps
            self.clock.tick()
            
            # Inputs
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True

            # Logic
            # 1) Copy calcbuff to display buff
            # 2) Update calcbuff to reflect next state of display buff
            #self.dispBuff = deepcopy(self.calcBuff)
            self.dispBuff = [[0 for i in range(PLAY_WIDTH)] for j in range(PLAY_HEIGHT)]
            
            for i, val in enumerate(self.calcBuff):
                for j, val2 in enumerate(val):
                    self.dispBuff[i][j] = val2
                    
            for dy in range(PLAY_HEIGHT-1):
                for dx in range(PLAY_WIDTH-1):
                    self.calcBuff[dy][dx] = self.deadOrAlive(dy,dx)
            
          
            # Drawing - draw display buffer
            self.DS.fill(BLACK)
            for y in range(0,PLAY_HEIGHT):
                for x in range(0,PLAY_WIDTH):
                    if self.dispBuff[y][x] != 0:
                        self.cellColour = RED
                        self.lifeRect = pg.Rect(x*PIX_SIZE,y*PIX_SIZE,PIX_SIZE,PIX_SIZE)
                        pg.draw.rect(self.DS,self.cellColour,self.lifeRect, 0)
                   
            
                    

            self.screen.blit(self.DS,(0,0))
            pg.display.flip()

            # Little loop to show starting point for preset patterns.
            while space == 0:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            space = 1

#Main
pg.init()
game = Seeds("Seeds")
game.mainLoop()
pg.quit()
