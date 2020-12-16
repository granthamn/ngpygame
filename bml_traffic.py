import pygame as pg
import random
from bmlconsts import *

# BML Traffic - red cells move L->R, blue cells move U->D, Taking it in turns

class Traffic:
    def __init__(self,caption):
        self.screen  = pg.display.set_mode(WINSIZE)
        self.DS = pg.Surface(WINSIZE)
        self.clock = pg.time.Clock()
        pg.display.set_caption(caption)
        self.quit = False
        self.turn = turn.BLUE
        self.blueDict = {}
        self.redDict = {}
        self.blueJammed = False
        self.redJammed = False
        

        

        # Initialise starting buffer with a certain percentage of "traffic" that is red
        # and a certain percentage that is blue
        blueCellsToUpdate = ((PLAY_WIDTH * PLAY_HEIGHT) / 100) * BLUEPERCENT
        redCellsToUpdate = ((PLAY_WIDTH * PLAY_HEIGHT)  / 100) * REDPERCENT

        
        while blueCellsToUpdate:
            randX = random.randint(0,PLAY_WIDTH-1)
            randY = random.randint(0,PLAY_HEIGHT-1)
            coOrd = (randX,randY)
            if coOrd not in self.blueDict and coOrd not in self.redDict:
                self.blueDict[coOrd] = 1
                blueCellsToUpdate -= 1

        while redCellsToUpdate:
            randX = random.randint(0,PLAY_WIDTH-1)
            randY = random.randint(0,PLAY_HEIGHT-1)
            coOrd = (randX,randY)
            if coOrd not in self.blueDict and coOrd not in self.redDict:
                self.redDict[coOrd] = 1
                redCellsToUpdate -= 1

    def checkAndMove(self,x,y,colDict,colDict2):

        coordList = []
        
      
        for k in colDict:
            if colDict[k] != 0:
                colVal = 0
                colVal2 = 0
            #print(k)
                posToCheck = ((k[0]+x) % (PLAY_WIDTH-1), (k[1]+y) % (PLAY_HEIGHT - 1))
                inCol = posToCheck in colDict
                inCol2 = posToCheck in colDict2
                if inCol:
                    colVal = colDict[posToCheck]
                if inCol2:
                    colVal2 = colDict2[posToCheck]

                if (not inCol2 and not inCol) or (colVal + colVal2 == 0):
                    colDict[k] = 0
                    coordList.append(posToCheck)
        
            

        for coOrd in coordList:
            colDict[coOrd] = 1

    def moveTraffic(self):
        
        # Move red traffic right unless it can't move
        # If space is empty, can move.
        # If space isn't empty, can't move
        #
        # Move blue traffic down unless it can't move
        if self.turn == turn.BLUE:
            self.checkAndMove(0,1,self.blueDict, self.redDict)
            self.turn = turn.RED
        else:
            self.checkAndMove(1,0,self.redDict,self.blueDict)
            self.turn = turn.BLUE
        
    def mainLoop(self):
        space = 0
        while not self.quit:
            #Timings - 20fps
            self.clock.tick()

              # Inputs
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True

            
            # Drawing
            self.DS.fill(WHITE)
            
            for k,v in self.redDict.items():
                if v != 0:
                    self.carRect = pg.Rect(k[0]*PIX_SIZE,k[1]*PIX_SIZE,PIX_SIZE,PIX_SIZE)
                    pg.draw.rect(self.DS,RED,self.carRect)
           
            for keys, items in self.blueDict.items():
                if items != 0:
                    self.carRect = pg.Rect(keys[0]*PIX_SIZE,keys[1]*PIX_SIZE,PIX_SIZE,PIX_SIZE)
                    pg.draw.rect(self.DS,BLUE,self.carRect)
                   
            

            self.screen.blit(self.DS,(0,0))
            
            pg.display.flip()

            # Logic
            self.moveTraffic()
            
            # Little loop to show starting point for preset patterns.
            while space == 0:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            space = 1

#Main
pg.init()
game = Traffic("BML Traffic")
game.mainLoop()
pg.quit()
