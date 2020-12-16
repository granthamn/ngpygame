import pygame as pg
import time
import math

WINSIZE = (1280,800)
BLACK=(0,0,0)
GREEN=(0,255,50)
DARKGREEN=(0,100,0)
RED=(255,0,0)
WHITE=(255,255,255)
GREY=(180,180,180)
LIGHTBLUE=(0,80,200)
PIXSIZE=8
DISPWIDTH=WINSIZE[0] // PIXSIZE
DISPHEIGHT=WINSIZE[1] // PIXSIZE


class car(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 0.0

        self.image = pg.image.load("img/car1.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.travelled = 0.0
        
   
        
    def slowDown(self,num):
        self.speed -= num

        
    def speedUp(self,num):
        self.speed += num
    def setXPos(self,num):
        self.xPos = self.xPos + num
        self.rect.x = self.xPos
    def setAbsXPos(self,num):
        self.xPos = num
        self.rect.x = num
    def setAbsYPos(self,num):
        self.yPos = num
        self.rect.y = num
    def getImWidth(self):
        return self.image.get_width()
    def setTravelled(self,num):
        self.travelled += num
    def getTravelled(self):
        return self.travelled
    def getSpeed(self):
        return self.speed
    def setAbsSpeed(self,num):
        self.speed = num
    
    
        
        

class RaceGame:
    def __init__(self, caption):
        self.highScore = 0
        self.lapTime = 0
        self.quitGame = False
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(WINSIZE)
        self.DS = pg.Surface(WINSIZE)
        pg.display.set_caption(caption)
        self.theCar = car()
        self.spriteList = pg.sprite.Group()
        self.spriteList.add(self.theCar)
        self.DS.fill(LIGHTBLUE)
        

        self.trackMiddle = 0.5
        self.roadWidth = 0.6
        self.clipWidth = self.roadWidth * 0.15
        self.roadWidth *= 0.5

        self.trackCurv = 0.0

        self.theCar.setAbsXPos(WINSIZE[0] / 2 - self.theCar.getImWidth() / 2)
        self.theCar.setAbsYPos(680)

        self.theTrack=[(0.0,10.0),(0.0,200.0),(2.0,200.0),(0.0,300.0),(-2.0,200.0),(0.5,250.0),(0.0,400.0),(-4.5,150.0),(0.0,200.0)]
        
    def handleEvents(self):
        #print(self.theCar.getSpeed())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quitGame = True
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.theCar.setXPos(-15)
        if keys[pg.K_UP]:
            self.theCar.speedUp(2.0 * self.elapsedTime)
            
        else:
            self.theCar.slowDown(1.0 * self.elapsedTime)
            
        if keys[pg.K_RIGHT]:
            self.theCar.setXPos(15)
        if keys[pg.K_DOWN]:
            self.theCar.slowDown(2.0)
                
        if self.theCar.getSpeed() < 0.0:
            self.theCar.setAbsSpeed(0.0)
        elif self.theCar.getSpeed() > 2.0:
            self.theCar.setAbsSpeed(2.0)

        self.theCar.setTravelled((70.0 * self.theCar.getSpeed()) * self.elapsedTime)
        
    def doUpdates(self):
        pass
    
    def drawTrack(self):

        trackOff = 0.0
        trackSect = 0

        while (trackSect < len(self.theTrack) and trackOff < self.theCar.getTravelled()):
            trackOff += self.theTrack[trackSect][1]
            trackSect += 1

        targetCurv = self.theTrack[trackSect-1][0]

        trackCurvDiff = (targetCurv - self.trackCurv) * self.elapsedTime * self.theCar.getSpeed()
        self.trackCurv += trackCurvDiff
        #print(self.trackCurv)
        
        for y in range(DISPHEIGHT // 2, DISPHEIGHT):
            for x in range(DISPWIDTH):
                
                roadPersp = float(float(y) /  ( DISPHEIGHT ))
                self.trackMiddle = 0.5 + self.trackCurv * math.pow(1.0 - roadPersp,3)
                
                self.roadWidth = 0.1 + roadPersp * 0.6

                self.clipWidth = self.roadWidth * 0.1
                self.roadWidth *= 0.3
                
                leftGrass = int((self.trackMiddle - self.roadWidth - self.clipWidth) * DISPWIDTH)
                leftClip = int((self.trackMiddle - self.roadWidth) * DISPWIDTH)
                rightClip = int((self.trackMiddle + self.roadWidth) * DISPWIDTH)
                rightGrass = int((self.trackMiddle + self.roadWidth + self.clipWidth) * DISPWIDTH)
                #print(leftGrass,leftClip,rightGrass,rightClip)
                #print(self.roadWidth)

                grassVal = math.sin(80.0 * math.pow(1.0 - roadPersp, 3) + self.theCar.getTravelled() * 0.1)
                clipVal = math.sin(180.0 * math.pow(1.0 - roadPersp, 2) + self.theCar.getTravelled())
                #print(grassVal)
                if grassVal < 0.65:
                    grassCol = DARKGREEN
                else:
                    grassCol = GREEN
                if clipVal < .85:
                    clipCol = RED
                else:
                    clipCol = WHITE
                if (x >= 0 and x < leftGrass) or (x >= rightGrass and x < DISPWIDTH):
                    drawCol = grassCol
                elif (x >= leftGrass and x < leftClip) or (x >= rightClip and x < rightGrass):
                    drawCol = clipCol
                else: 
                    drawCol = GREY
                
                topLeft = (x * PIXSIZE,y * PIXSIZE)
                rectSize = (PIXSIZE,PIXSIZE)
                drawRect = pg.Rect(topLeft,rectSize)
                pg.draw.rect(self.DS,drawCol,drawRect)
                
        self.screen.blit(self.DS,(0,0))
            
        
    def play(self):
        self.theTimer = time.monotonic()
        while not self.quitGame:
            # Timing
            #self.clock.tick(60)
            self.theTimer2 = time.monotonic()
            self.elapsedTime = self.theTimer2 - self.theTimer
            self.theTimer = self.theTimer2
            
            #Input
            self.handleEvents()
            
            # Logic
            self.doUpdates()

            # Rendering
            #self.screen.fill(LIGHTBLUE)
            self.drawTrack()
            self.drawTheCar(self.screen)
            pg.display.flip()
            

    def drawTheCar(self,surf):
        self.spriteList.draw(surf)

#Main
pg.init()
game = RaceGame("Race")
game.play()
pg.quit()
