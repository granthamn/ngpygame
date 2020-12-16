import pygame as pg
import random
from lifeConsts import *
from copy import deepcopy


class GameOfLife:
    def __init__(self,caption):
        self.DS  = pg.display.set_mode(WINSIZE)
        self.clock = pg.time.Clock()
        pg.display.set_caption(caption)
        self.quit = False
        

        # 2 Buffers - display and calc
        self.calcBuff = [[random.randint(0,1) for x in range(PLAY_WIDTH)] for y in range (PLAY_HEIGHT)]
        #self.dispBuff = [[0 for x in range(WINSIZE[0] // PIX_SIZE)] for y in range (WINSIZE[1] // PIX_SIZE)]

    def deadOrAlive(self,py,px):
        # For each neighbouring cell (in 8 directions) calculate how many neighbours, then apply rule to say
        # if it will next be dead or alive.
        # Rules:1) If an alive cell has 2 or 3 neighbours, it stays alive
        #       2) If an alive cell has less than 2 or more than 3 neighbours, it dies
        #       3) If a dead cell has exactly 3alive neighbours, it becomes alive.
        state = 0
        #print(y,x)
        neighbours = self.dispBuff[py-1][px-1] + self.dispBuff[py-1][px] + self.dispBuff[py-1][px+1]  \
                   + self.dispBuff[py][px-1]   + 0                    + self.dispBuff[py][px+1]    \
                   + self.dispBuff[py+1][px-1] + self.dispBuff[py+1][px] + self.dispBuff[py+1][px+1]

        if self.dispBuff[py][px] == 0:
            if neighbours == 3:
                #It's a miracle!
                state = 1
        else:
            if neighbours == 2 or neighbours == 3:
                # It survived
                state = 1
            
                

        return state
        
    def mainLoop(self):

        while not self.quit:
            #Timings
            self.clock.tick(20)
            
            # Inputs
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True
            # Logic
            # Investigage using numpy instead of list of lists
            # 1) Copy calcbuff to display buff
            # 2) Update calcbuff to reflect next state of display buff
            self.dispBuff = deepcopy(self.calcBuff)
            for dy in range(1,PLAY_HEIGHT-1):
                for dx in range(1,PLAY_WIDTH-1):
                    self.calcBuff[dy][dx] = self.deadOrAlive(dy,dx)
            #self.calcBuff = [[self.deadOrAlive(dy,dx) for dx in range(1,(PLAY_WIDTH-1))] for dy in range(1,(PLAY_HEIGHT-1))]
            #print(len(self.calcBuff))
            
            

            # Drawing - draw display buffer
            self.DS.fill(BLACK)
            for y in range(0,PLAY_HEIGHT):
                for x in range(0,PLAY_WIDTH):
                    if self.dispBuff[y][x] == 0:
                        self.cellColour = BLACK
                    else:
                        self.cellColour = WHITE
                    self.lifeRect = pg.Rect(y*PIX_SIZE,x*PIX_SIZE,PIX_SIZE,PIX_SIZE)
                    pg.draw.rect(self.DS,self.cellColour,self.lifeRect)
    
            pg.display.update()
        

#Main
pg.init()
game = GameOfLife("Conway's Game of Life")
game.mainLoop()
pg.quit()
