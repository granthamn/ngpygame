import pygame as pg
import random
from copy import deepcopy
from loopConsts import *
from collections import defaultdict
import cProfile

# Langtons Loops Automata

class langLoops:
    def __init__(self,caption):
        self.screen  = pg.display.set_mode(WINSIZE) 
        self.DS = pg.Surface(WINSIZE)
        self.clock = pg.time.Clock()
        pg.display.set_caption(caption)
        self.quit = False
        # Starting point to insert starting grid
        self.offX = 40
        self.offY = 44
        # Limit of cells we need to calculate rules for to hopefully to improve performance)
        self.xLimit = len(startLoop[9]) + 2
        self.yLimit = len(startLoop) + 1
        self.minX = self.offX - 1
        self.maxX = self.offX + self.xLimit
        self.minY = self.offY
        self.maxY = self.offY + self.yLimit
        self.ruleDict = defaultdict(list)
        for r in ruleSet:
            s = r[:5]
            self.ruleDict[s].append(r)
        
        # Initialise screen buffer
        self.calcBuff = [[0 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]
       
        # Copy starting set to screen buffer
        for y in range(len(startLoop)):
            for x in range(len(startLoop[y])):
                self.calcBuff[y+self.offY][x+self.offX] = int(startLoop[y][x])
       

    def calcNewCellValue(self,y,x):
        # Get cell value and list of rules starting with that value
        # For each search for all neighbour values in rule set
        # If matching rule, change cell value.
        #All of the above needs to be done on a copy of the buffer as all
        # cells need to change at the same time
        # If there is no exact match for the rule, check for combinations of the 4 neigbours to locate a match.
        
        surrBuff = []
        surrBuff.append(str(self.dispBuff[y][x]) + str(self.dispBuff[y-1][x]) + str(self.dispBuff[y][x+1]) + str(self.dispBuff[y+1][x]) + str(self.dispBuff[y][x-1]))
        surrBuff.append(str(self.dispBuff[y][x]) + str(self.dispBuff[y][x+1]) + str(self.dispBuff[y+1][x]) + str(self.dispBuff[y][x-1]) + str(self.dispBuff[y-1][x]))
        surrBuff.append(str(self.dispBuff[y][x]) + str(self.dispBuff[y+1][x]) + str(self.dispBuff[y][x-1]) + str(self.dispBuff[y-1][x]) + str(self.dispBuff[y][x+1]))
        surrBuff.append(str(self.dispBuff[y][x]) + str(self.dispBuff[y][x-1]) + str(self.dispBuff[y-1][x]) + str(self.dispBuff[y][x+1]) + str(self.dispBuff[y+1][x]))
        

        matchSet = []
        
        for buff in surrBuff:  
            matchSet = self.ruleDict[buff]
            
            if len(matchSet) > 0:
                break
        
            
        #print("Match",matchSet)
        
        if int(matchSet[0][5]) != self.dispBuff[y][x]:
            #print("Changing", x,y, "From", self.dispBuff[y][x], "To", matchSet[0][5])
            if x == self.maxX and self.maxX < PLAY_WIDTH:
                self.maxX += 1
            if x == self.minX and self.minX > 0:
                self.minX -=1
            if y == self.maxY and self.maxY < PLAY_HEIGHT:
                self.maxY += 1
            if y == self.minY and self.minY > 0:
                self.minY -= 1
        return int(matchSet[0][5])
                                   
        
                                                                
    def updateCalcBuff(self):
        
            # For each cell within bounds.
            for y in range(self.minY,self.maxY+1):
                for x in range(self.minX,self.maxX+1):
                    self.calcBuff[y][x] = self.calcNewCellValue(y,x)
        
    def draw(self):
        for y in range(self.minY,self.maxY+1):
            for x in range(self.minX,self.maxX+1):
                pg.draw.circle(self.DS,COLOURS[self.dispBuff[y][x]],(x*PIX_SIZE,y*PIX_SIZE),RAD)
        
        
    def mainLoop(self):
        space = 0
        self.dispBuff = deepcopy(self.calcBuff)
        self.DS.fill(GREY)
        for y in range(PLAY_HEIGHT):
            for x in range(PLAY_WIDTH):
                #print(self.dispBuff[y][x])
                pg.draw.circle(self.DS,COLOURS[self.dispBuff[y][x]],(x*PIX_SIZE,y*PIX_SIZE),RAD)
        self.screen.blit(self.DS,(0,0))
        pg.display.flip()
        
        while not self.quit:
            #Timings - 20fps
            self.clock.tick(20) 


            self.updateCalcBuff()
            self.dispBuff = deepcopy(self.calcBuff)
               
            # Drawing
            self.draw()
            self.screen.blit(self.DS,(0,0))            
            pg.display.flip()

            # Inputs
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True
            
                     
            
            # Little loop to show starting point for preset patterns.
            while space == 0:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            space = 1

#Main
pg.init()
game = langLoops("Langton's Loops")
cProfile.run('game.mainLoop()')
pg.quit()
