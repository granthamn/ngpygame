import pygame as pg
import random
from langConsts import *
from copy import deepcopy


class Langton:
    def __init__(self,caption):
        self.DS  = pg.display.set_mode(WINSIZE)
        self.clock = pg.time.Clock()
        pg.display.set_caption(caption)
        self.quit = False
        # Choose a random starting point for our 'ANT'
        self.antX = random.randint(0,PLAY_WIDTH-1)
        self.antY = random.randint(0,PLAY_HEIGHT-1)
        # Start ant facing up
        self.antDir = DIR.LEFT 

      
        # Uncomment next line for a Randomised starting state
        #self.dispBuff = [[random.randint(0,1) for x in range(PLAY_WIDTH)] for y in range (PLAY_HEIGHT)]
        # Uncomment next line for an all black starting point
        #self.dispBuff = [[0 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]
        # Uncomment next line for an all white starting point
        self.dispBuff = [[1 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]

        print(len(self.dispBuff),len(self.dispBuff[0]))

    def moveAnt(self,antPosCol): 
        #If the ant moves offscreen he will warp back to the other side
        if antPosCol == 1:
            antRot = 1
        else:
            antRot = -1
          
        # Convert a 90 or -90 degree rotation into the next direction
        self.antDir = DIR((self.antDir.value + antRot) % 4)

        # Next step - update ant pos based on direction
        if self.antDir == DIR.UP:
            if self.antY == 0:
                self.antY = PLAY_HEIGHT - 1
            else:
                self.antY -= 1
        elif self.antDir == DIR.RIGHT:
            if self.antX == PLAY_WIDTH - 1:
                self.antX = 0
            else:
                self.antX += 1
        elif self.antDir == DIR.DOWN:
            if self.antY == 0:
                self.antY = PLAY_HEIGHT -1
            else:
                self.antY += 1
        else:
            if self.antX == 0:
                self.antX = PLAY_WIDTH - 1
            else:
                self.antX -= 1
                
        
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
            antPosCol = self.dispBuff[self.antY][self.antX]
            
            if antPosCol == 1:
                cellCol = 0
            else:
                cellCol = 1

            self.dispBuff[self.antY][self.antX] = cellCol
            self.moveAnt(antPosCol)
            
            
            
          
            # Drawing - draw display buffer
            self.DS.fill(BLACK)
            for y in range(0,PLAY_HEIGHT):
                for x in range(0,PLAY_WIDTH):
                    if self.dispBuff[y][x] == 0:
                        self.cellColour = BLACK
                    else:
                        self.cellColour = WHITE
                      
                    self.antRect = pg.Rect(x*PIX_SIZE,y*PIX_SIZE,PIX_SIZE,PIX_SIZE)
                    pg.draw.rect(self.DS,self.cellColour,self.antRect)
    
            pg.display.update()

            # Little loop to show starting point for preset patterns.
            while space == 0:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            space = 1

#Main
pg.init()
game = Langton("Langton's Ant")
game.mainLoop()
pg.quit()
