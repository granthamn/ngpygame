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
        # Uncomment next line for a Randomised starting state
        #self.calcBuff = [[random.randint(0,1) for x in range(PLAY_WIDTH)] for y in range (PLAY_HEIGHT)]
        # Uncomment next line for a blank starting point followed by a set pattern
        self.calcBuff = [[0 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]   

        # Uncomment one of the following blocks to start with a known pattern to create interesting patterns.
        # R-pentomino
        #self.calcBuff[20][40] = 1
        #self.calcBuff[20][41] = 1
        #self.calcBuff[21][39] = 1
        #self.calcBuff[21][40] = 1
        #self.calcBuff[22][40] = 1

        #Die hard
        #self.calcBuff[20][40] = 1
        #self.calcBuff[20][41] = 1
        #self.calcBuff[21][41] = 1
        #self.calcBuff[21][45] = 1
        #self.calcBuff[21][46] = 1
        #self.calcBuff[21][47] = 1
        #self.calcBuff[19][46] = 1

        #Acorn
        #self.calcBuff[20][40] = 1
        #self.calcBuff[20][41] = 1
        #self.calcBuff[18][41] = 1
        #self.calcBuff[19][43] = 1
        #self.calcBuff[20][44] = 1
        #self.calcBuff[20][45] = 1
        #self.calcBuff[20][46] = 1

        # Gosper Glider Gun
        self.calcBuff[20][40] = 1
        self.calcBuff[20][41] = 1
        self.calcBuff[21][40] = 1
        self.calcBuff[21][41] = 1
        self.calcBuff[20][50] = 1
        self.calcBuff[21][50] = 1
        self.calcBuff[22][50] = 1
        self.calcBuff[19][51] = 1
        self.calcBuff[23][51] = 1
        self.calcBuff[18][52] = 1
        self.calcBuff[18][53] = 1
        self.calcBuff[24][52] = 1
        self.calcBuff[24][53] = 1
        self.calcBuff[21][54] = 1
        self.calcBuff[19][55] = 1
        self.calcBuff[23][55] = 1
        self.calcBuff[20][56] = 1
        self.calcBuff[21][56] = 1
        self.calcBuff[22][56] = 1
        self.calcBuff[21][57] = 1
        self.calcBuff[18][60] = 1
        self.calcBuff[19][60] = 1
        self.calcBuff[20][60] = 1
        self.calcBuff[18][61] = 1
        self.calcBuff[19][61] = 1
        self.calcBuff[20][61] = 1
        self.calcBuff[17][62] = 1
        self.calcBuff[21][62] = 1
        self.calcBuff[17][64] = 1
        self.calcBuff[16][64] = 1
        self.calcBuff[21][64] = 1
        self.calcBuff[22][64] = 1
        self.calcBuff[18][74] = 1
        self.calcBuff[19][74] = 1
        self.calcBuff[18][75] = 1
        self.calcBuff[19][75] = 1
        
    def deadOrAlive(self,py,px):
        # For each neighbouring cell (in 8 directions) calculate how many neighbours, then apply rule to say
        # if it will next be dead or alive.
        # Rules:1) If an alive cell has 2 or 3 neighbours, it stays alive
        #       2) If an alive cell has less than 2 or more than 3 neighbours, it dies
        #       3) If a dead cell has exactly 3alive neighbours, it becomes alive.
        state = 0
        # Count actuve neighbours
        neighbours = self.dispBuff[py-1][px-1] + self.dispBuff[py-1][px] + self.dispBuff[py-1][px+1]  \
                   + self.dispBuff[py][px-1]   + 0                       + self.dispBuff[py][px+1]    \
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
        space = 0
        while not self.quit:
            #Timings - 20fps
            self.clock.tick(20)
            
            # Inputs
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True

            # Logic
            # 1) Copy calcbuff to display buff
            # 2) Update calcbuff to reflect next state of display buff
            self.dispBuff = deepcopy(self.calcBuff)
            for dy in range(1,PLAY_HEIGHT-1):
                for dx in range(1,PLAY_WIDTH-1):
                    self.calcBuff[dy][dx] = self.deadOrAlive(dy,dx)
            
          
            # Drawing - draw display buffer
            self.DS.fill(BLACK)
            for y in range(0,PLAY_HEIGHT):
                for x in range(0,PLAY_WIDTH):
                    if self.dispBuff[y][x] != 0:
                        self.cellColour = GREEN
                        self.lifeRect = pg.Rect(x*PIX_SIZE,y*PIX_SIZE,PIX_SIZE,PIX_SIZE)
                        pg.draw.rect(self.DS,self.cellColour,self.lifeRect)
    
            pg.display.update()

            # Little loop to show starting point for preset patterns.
            while space == 0:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            space = 1

#Main
pg.init()
game = GameOfLife("Conway's Game of Life")
game.mainLoop()
pg.quit()
