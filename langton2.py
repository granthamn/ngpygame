import pygame as pg
import random
from langConsts import *
from copy import deepcopy


class ant:
    def __init__(self):
        # Choose a random starting point for our 'ANT'
        self.x = random.randint(0,PLAY_WIDTH-1)
        self.y = random.randint(0,PLAY_HEIGHT-1)
        # Start ant facing left
        self.dir = DIR.LEFT
        # Rotation - 1=Clock,-1=AntiClock
        self.rot = 1

        self.loadAntImages()

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def getDir(self):
        return self.dir

    def loadAntImages(self):
        self.sSheetImage = pg.image.load("img/ants3.png").convert()
        self.antImages = []
        for i in range(0,4):
            rect = pg.Rect(0,i * ANTSIZE,ANTSIZE,ANTSIZE)
            image = pg.Surface(rect.size).convert()
            image.blit(self.sSheetImage,(0,0),rect)
            image.set_colorkey(image.get_at((0,0)))
            
            self.antImages.append(image)
       
    def draw(self,DS):
        DS.blit(self.antImages[self.dir.value],(self.x * PIX_SIZE , self.y * PIX_SIZE))

    def move(self,posCol):
        # If ant is on a white square, rotate clock else rotate anti-clock
        if posCol == 1:
            self.rot = 1
        else:
            self.rot = -1

    def setDir(self):
        # DIR - 0 - UP, 1 - RIGHT, 2 - DOWN, 3 - LEFT
        # By adding or subtracting 1 depending on rot and modulus 4,
        # we rotate 0,1,2,3 in either direction to determine next direction
        self.dir = DIR((self.dir.value + self.rot) % 4)

    def setNextPos(self):
        
        #  update ant pos based on direction
        if self.dir == DIR.UP:
            if self.y == 0:
                self.y = PLAY_HEIGHT - 1
            else:
                self.y -= 1
        elif self.dir == DIR.RIGHT:
            if self.x == PLAY_WIDTH - 1:
                self.x = 0
            else:
                self.x += 1
        elif self.dir == DIR.DOWN:
            if self.y == PLAY_HEIGHT-1:
                self.y = 0
            else:
                self.y += 1
        else:
            if self.x == 0:
                self.x = PLAY_WIDTH - 1
            else:
                self.x -= 1

class Langton:
    def __init__(self,caption):
        self.DS  = pg.display.set_mode(WINSIZE)
        self.clock = pg.time.Clock()
        pg.display.set_caption(caption)
        self.antSteps = 0
        self.quit = False
        self.theAnt = ant()
        self.antFont = pg.font.SysFont("Arial",12,True)
               

      
        # Uncomment next line for a Randomised starting state
        #self.dispBuff = [[random.randint(0,1) for x in range(PLAY_WIDTH)] for y in range (PLAY_HEIGHT)]
        # Uncomment next line for an all black starting point
        #self.dispBuff = [[0 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]
        # Uncomment next line for an all white starting point
        self.dispBuff = [[1 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]


    def moveAnt(self,antPosCol):

        self.theAnt.move(antPosCol)
          
        # Convert a 90 or -90 degree rotation into the next direction
        self.theAnt.setDir()
        # Next step - update ant pos based on direction
        self.theAnt.setNextPos()

        
    def drawSteps(self):
        self.stepsText = self.antFont.render("Steps: " + str(self.antSteps),True,RED)
        self.dirText = self.antFont.render("DIR:" + str(self.theAnt.getDir()),True,RED)
        self.DS.blit(self.stepsText,(50,20))
        self.DS.blit(self.dirText,(50,40))
        
    def mainLoop(self):
        
        space = 0
        # Draw Ant starting position
        
        
        
        while not self.quit:
            #Timings - 20fps
            self.clock.tick()
            
            # Inputs
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True

 
          
            # Drawing - draw display buffer
            #self.DS.fill(BLACK)
            for y in range(0,PLAY_HEIGHT):
                for x in range(0,PLAY_WIDTH):
                    if self.dispBuff[y][x] == 0:
                        self.cellColour = BLACK
                    else:
                        self.cellColour = WHITE
                      
                    self.antRect = pg.Rect(x*PIX_SIZE,y*PIX_SIZE,PIX_SIZE,PIX_SIZE)
                    pg.draw.rect(self.DS,self.cellColour,self.antRect)
            self.theAnt.draw(self.DS)
            self.drawSteps()
            
            pg.display.update()

            # Logic - update ant etc after drawing intial pos

            antPosCol = self.dispBuff[self.theAnt.getY()][self.theAnt.getX()]
            
            #print(self.theAnt.getX(),self.theAnt.getY())
            if antPosCol == 1:
                cellCol = 0
            else:
                cellCol = 1

            self.dispBuff[self.theAnt.getY()][self.theAnt.getX()] = cellCol
            self.moveAnt(antPosCol)
            self.antSteps += 1
            

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
