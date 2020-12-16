import pygame as pg
import random
from brainconsts import *
from copy import deepcopy
from copy import copy


class BriansBrain:
    def __init__(self,caption):
        self.screen  = pg.display.set_mode(WINSIZE)
        self.DS = pg.Surface(WINSIZE)
        self.clock = pg.time.Clock()
        pg.display.set_caption(caption)
        self.quit = False

        

        # 2 Buffers - display and calc
        # Uncomment next line for a Randomised starting state
        #self.calcBuff = [[random.randint(0,2) for x in range(PLAY_WIDTH-1)] for y in range (PLAY_HEIGHT-1)]
        #self.calcDict = {([x for x in range(PLAY_WIDTH)],[y for y in range(PLAY_HEIGHT)]): random.randint(0,2)}
        #self.calcDict = dict.fromkeys((x for x in range(PLAY_HEIGHT),y for y in range(PLAY_WIDTH)),random.randint(0,2))
        self.calcDict = {}
        for y in range(PLAY_HEIGHT):
            for x in range(PLAY_WIDTH):
                self.calcDict[(y,x)] = random.randint(0,2)
                
        #self.calcDict = { tuple(range(PLAY_HEIGHT),range(PLAY_WIDTH)) : random.randint(0,2)}
        #print(self.calcDict)
        # Uncomment next line for a blank starting point followed by a set pattern
        #self.calcBuff = [[0 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]   

        # Randomise a 10 * 10 grid of either alive or dying cells
       # for y in range(40):
        #    for x in range(40):
         #       self.calcBuff[35+y][45+x] = random.randint(0,2)
        

        
    def deadOrAlive(self,py,px):
        # There are 3 states - Dead = 0, Dying = 1, Alive = 2
        # Rules:
        # A dead cell becomes alive if it has exactly two alive neighbours.
        # Alive cells become dying
        # Dying cells become dead
        state = 0
        # Count alive neighbours
        twoCount = 0
       

        for y in range(-1,2):
            for x in range(-1,2):
                if y != 0 or x != 0:
                    if self.dispDict[(py+y) % (PLAY_HEIGHT-1),(px+x) % (PLAY_WIDTH -1) ] == 2:
                        twoCount += 1
        
        if self.dispDict[py,px] == 0:
            if twoCount == 2:
                #It's a miracle!
                state = 2
        elif self.dispDict[py,px] == 1:
            # Sorry he's not going to make it
            state = 0 
        else:
            # He's not got long
            state = 1 
            
            
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
            #self.dispBuff = [[0 for i in range(PLAY_WIDTH)] for j in range(PLAY_HEIGHT)]
            self.dispDict = self.calcDict.copy()
            
            #for i, val in enumerate(self.calcBuff):
            #    for j, val2 in enumerate(val):
            #        self.dispBuff[i][j] = val2
                    
            
               
            for key in self.calcDict:
                self.calcDict[key] = self.deadOrAlive(key[0],key[1])
          
            # Drawing - draw display buffer
            self.DS.fill(BLACK)
            for key in self.dispDict:
                if self.dispDict[key] == 1:
                    self.cellColour = BLUE
                    self.lifeRect = pg.Rect(key[1]*PIX_SIZE,key[0]*PIX_SIZE,PIX_SIZE,PIX_SIZE)
                    pg.draw.rect(self.DS,self.cellColour,self.lifeRect, 0)
                elif self.dispDict[key] == 2:
                    self.cellColour = WHITE           
                    self.lifeRect = pg.Rect(key[1]*PIX_SIZE,key[0]*PIX_SIZE,PIX_SIZE,PIX_SIZE)
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
game = BriansBrain("Brian's Brain")
game.mainLoop()
pg.quit()
