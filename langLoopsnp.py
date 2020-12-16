import pygame as pg
import random
from copy import deepcopy
from loopConstsNp import *
import numpy as np
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
        self.offX = 24
        self.offY = 34
        # Limit of cells we need to calculate rules for to hopefully to improve performance)
        self.xLimit = len(startLoop[9]) + 2
        self.yLimit = len(startLoop) + 1
        self.minX = self.offX - 1
        self.maxX = self.offX + self.xLimit
        self.minY = self.offY
        self.maxY = self.offY + self.yLimit
        
        # Initialise screen buffer
        #self.calcBuff = [[0 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]
        self.calcBuff = np.zeros((PLAY_HEIGHT,PLAY_WIDTH))
       
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
        
        #dispX = self.offX + x
        #dispY = self.offY + y
        #pg.draw.circle(self.screen,WHITE,(x*PIX_SIZE,y*PIX_SIZE),PIX_SIZE // 2)
        #pg.display.flip()
        surrBuff = []
        surrBuff.append(str(self.dispBuff[y][x]) + str(self.dispBuff[y-1][x]) + str(self.dispBuff[y][x+1]) + str(self.dispBuff[y+1][x]) + str(self.dispBuff[y][x-1]))
        surrBuff.append(str(self.dispBuff[y][x]) + str(self.dispBuff[y][x+1]) + str(self.dispBuff[y+1][x]) + str(self.dispBuff[y][x-1]) + str(self.dispBuff[y-1][x]))
        surrBuff.append(str(self.dispBuff[y][x]) + str(self.dispBuff[y+1][x]) + str(self.dispBuff[y][x-1]) + str(self.dispBuff[y-1][x]) + str(self.dispBuff[y][x+1]))
        surrBuff.append(str(self.dispBuff[y][x]) + str(self.dispBuff[y][x-1]) + str(self.dispBuff[y-1][x]) + str(self.dispBuff[y][x+1]) + str(self.dispBuff[y+1][x]))
        
        #print("Curr",y,x, self.dispBuff[y][x])
        #print("Surr",surrBuff)
        matchSet = []
        for buff in surrBuff:  
            #matchSet = [r for r in ruleSet if r.startswith(buff)]
            matchSet = [r for r in ruleSet if r[:5] == buff]
            
            
            if len(matchSet) > 0:
                break
        
            
        #print("Match",matchSet)
        
        if int(matchSet[0][5]) != self.dispBuff[y][x]:
            #print("Changing", x,y, "From", self.dispBuff[y][x], "To", matchSet[0][5])
            if x == self.maxX and self.maxX < PLAY_WIDTH:
                self.maxX += 1
                #print("Inc X", self.maxX)
            if x == self.minX and self.minX > 0:
                #print("Dec X",self.minX)
                #self.minX -=1
            if y == self.maxY and self.maxY < PLAY_HEIGHT:
                self.maxY += 1
                #print("IncY",self.maxY)
            if y == self.minY and self.minY > 0:
                self.minY -= 1
                #print("Dec Y",self.minY)
        return int(matchSet[0][5])
                                   
        
                                                                
    def updateCalcBuff(self):
        
            # For each cell within bounds.
            for y in range(self.minY,self.maxY+1):
                for x in range(self.minX,self.maxX+1):
                    self.calcBuff[y][x] = self.calcNewCellValue(y,x)
            #print("Calc",self.calcBuff)

    def draw(self):
        for y in range(self.minY,self.maxY+1):
            for x in range(self.minX,self.maxX+1):
                #print(self.dispBuff[y][x])
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
            #space = 0 
            #Timings - 20fps
            self.clock.tick(20) 


            self.updateCalcBuff()
            self.dispBuff = deepcopy(self.calcBuff)
               
            # Drawing
            #self.DS.fill(GREY)
            self.draw()
            self.screen.blit(self.DS,(0,0))            
            pg.display.flip()

            # Inputs
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True

            # Logic
      
           
            #print("Pre-Calc",self.calcBuff)
            
                     
            
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
