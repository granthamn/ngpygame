import pygame as pg
import random
from snakeConsts import *


class Menu:
    def __init__(self,caption):
        self.title = caption
        self.startString = "S - Start"
        self.quitString = "Q - Quit"
        self.dbString = "D - Allow double-back? - No"
        self.titleFont = pg.font.SysFont("Comic Sans", 32, True)
        self.optFont = pg.font.SysFont("Arial", 14, True)
        self.titleText = self.titleFont.render(self.title, True, GREEN)
        self.startText = self.optFont.render(self.startString, True, WHITE)
        self.quitText = self.optFont.render(self.quitString, True, WHITE)
        #self.dbText = self.optFont.render(self.dbString, True, WHITE)
        

    def setDbText(self, dbText):
        self.dbString = dbText

    def draw(self, DS):
        self.dbText = self.optFont.render(self.dbString, True, WHITE)
        DS.blit(self.titleText, (200,120))
        DS.blit(self.startText, (215, 160))
        DS.blit(self.dbText, (215, 180))
        DS.blit(self.quitText, (215, 200))
        


class SnakeGame:
    def __init__(self, caption):
        self.score = 0
        self.highScore = 0
        self.quitGame = False
        self.caption = caption
        self.DS = pg.display.set_mode(WINSIZE)
        self.clock = pg.time.Clock()
        self.fruitClock = pg.time.Clock()
        pg.display.set_caption(self.caption)
        self.font = pg.font.SysFont("Arial",12,True)
        self.fruit = Segment(SEGTYPE.FRUIT,BLUE, 5, 5)
        self.fruitTime = self.fruitClock.tick()
        self.allowDoubleBack = True
        
        
    def doMenu(self):
      
        self.menu = Menu(self.caption)
        while not self.quitGame:
            
            self.DS.fill(BLACK)
            
            self.menu.draw(self.DS)
            pg.display.update()
            
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_q:
                    self.quitGame = True
                if event.type == pg.KEYDOWN and event.key == pg.K_d:
                    if self.allowDoubleBack == True:
                        self.allowDoubleBack = False
                        self.menu.setDbText("D - Allow double-back? - Yes")
                    else:
                        self.allowDoubleBack = True
                        self.menu.setDbText("D - Allow double-back? - No")
                    
                if event.type == pg.KEYDOWN and event.key == pg.K_s:
                    self.play()
            
    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quitGame = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and (self.allowDoubleBack or not(self.snake.dir == DIR.RIGHT)):
                    self.snake.dir = DIR.LEFT
                elif event.key == pg.K_UP and (self.allowDoubleBack or not(self.snake.dir == DIR.DOWN)):
                    self.snake.dir = DIR.UP
                elif event.key == pg.K_RIGHT and (self.allowDoubleBack or not(self.snake.dir == DIR.LEFT)):
                    self.snake.dir = DIR.RIGHT
                elif event.key == pg.K_DOWN and (self.allowDoubleBack or not(self.snake.dir == DIR.UP)):
                    self.snake.dir = DIR.DOWN
                                 
    def doUpdates(self):
        
        # The idea will be to update the xPos and yPos of the last segment only and make it the head
        # Then draw the rest of the segments as they are
        
        
        self.snake.updatePos(self.allowDoubleBack)
        if self.snake.getStatus() != SNAKESTAT.DEAD:
            if self.snake.getCoord() == self.fruit.getCoord():
                self.snake.grow(self.allowDoubleBack)
                # Score is based on time between fruits and length of snake
                # So if you get fruit quicker, score for that fruit will be higher
                self.score += (len(self.snake.segments()) * 2)
                self.score += int(200000 // self.fruitClock.tick())
                #print(str(int(200000 // self.fruitClock.tick())))
                nextFruitLoc = self.chooseFruitLoc()
                self.fruit = Segment(SEGTYPE.FRUIT,BLUE,nextFruitLoc[0],nextFruitLoc[1])
        # This looks odd but we might be dead right after eating a fruit
        if self.snake.getStatus() == SNAKESTAT.DEAD:
            for seg in self.snake.segments():
                seg.setColour(BROWN)
    
    def chooseFruitLoc(self):
        
        validFruitLoc = False
        while not validFruitLoc:
            tempX, tempY = random.randint(0,19), random.randint(0,19)
            if (tempX, tempY) not in self.snake.getPos() or self.snake.getPos()[(tempX, tempY)] == 0:
                validFruitLoc = True
        return (tempX, tempY)
        
        

    def drawGrid(self,surface,pWidth,pHeight,sWidth,sHeight,colour):
        for y in range(0,pWidth+sWidth,sWidth):
            pg.draw.line(surface,colour,(0,y),(pWidth,y))
        for x in range(0,pHeight+sHeight,sHeight):
            pg.draw.line(surface,colour,(x,0),(x,pHeight))
            
    def debugDraw(self):
        self.xString = "X: " + str(self.snake.segList[0].x)
        self.yString = "Y: " + str(self.snake.segList[0].y)
        self.dirString = "DIR: " + str(self.snake.dir)
        self.scoreString = "Score: " + str(self.score)
        self.lenString = "Len: " + str(len(self.snake.segList))
        self.dieString = "Status: " + str(self.snake.status)
        self.xText = self.font.render(self.xString,True,WHITE)
        self.yText = self.font.render(self.yString,True, WHITE)
        self.dirText = self.font.render(self.dirString,True,WHITE)
        self.dieText = self.font.render(self.dieString,True,WHITE)
        self.lenText = self.font.render(self.lenString,True,WHITE)
        self.scoreText = self.font.render(self.scoreString, True, WHITE)
        self.DS.blit(self.xText,(PLAY_SIZE[0] + 20, 50))
        self.DS.blit(self.yText,(PLAY_SIZE[0] + 20, 70))
        self.DS.blit(self.dirText, (PLAY_SIZE[0] + 20, 90))
        self.DS.blit(self.lenText, (PLAY_SIZE[0] + 20, 110))
        self.DS.blit(self.scoreText,(PLAY_SIZE[0] + 20, 130))
        self.DS.blit(self.dieText, (50, PLAY_SIZE[0] + 20))

            
    def play(self):
        
        self.snake = Snake()
        
        while not self.quitGame and self.snake.getStatus() == SNAKESTAT.ALIVE:
            
            # Timing
            pg.time.delay(100)
            self.clock.tick(20)
        
            # Input
            if self.snake.getStatus() != SNAKESTAT.DEAD:
                self.handleEvents()
            
                # Logic
                self.doUpdates()

                # Rendering
            self.DS.fill(BLACK)
            self.snake.draw(self.DS)
            self.fruit.draw(self.DS)
            self.debugDraw()
            
    
            self.drawGrid(self.DS,PLAY_SIZE[0],PLAY_SIZE[1],PIX_WIDTH,PIX_HEIGHT,GREY)
            pg.display.update()

        if self.snake.getStatus() == SNAKESTAT.DEAD:
            pg.time.delay(3000)
        if self.quitGame:
            pg.quit()

class Snake:
    def __init__(self):
        self.length = 1
        self.xPos = 9
        self.yPos = 9
        self.coOrd = (self.xPos, self.yPos)
        self.dir = DIR.LEFT # 1 left, 2 up ,3 right, 4 down
        self.segList = []
        self.segList.append(Segment(SEGTYPE.HEAD,RED,self.xPos,self.yPos))
        # Maintain a dictionary of current occupied positions.
        # To be used for ensuring fruit spawns at an empty grid position.
        self.posDict = { (self.xPos,self.yPos) : 1}
        self.status = SNAKESTAT.ALIVE

    def getStatus(self):
        return self.status
    
    def getCoord(self):
        return self.coOrd

    def segments(self):
        return self.segList

    def getPos(self):
        return self.posDict
    def gerDir(self):
        return self.dir
    
    def updatePos(self,doubleBack):
        #Note - do dead status update in here! Get rid of other functions.
        for i in range (0,20):
            self.handleKeyWhenGrow(doubleBack)
        if len(self.segList) > 1:
            oldX = self.segList[0].x
            oldY = self.segList[0].y
            self.segList[0].setType(SEGTYPE.BODY)
            tempSeg = self.segList.pop()
            #print('TempXPreIns',tempSeg.x,'TempYPreIns',tempSeg.y)
            self.posDict[tempSeg.coOrd] = 0
            self.segList.insert(0,tempSeg)
            self.segList[0].setType(SEGTYPE.HEAD)
            self.segList[0].x = oldX
            self.segList[0].y = oldY
            self.segList[0].coOrd = (oldX, oldY)
            #print('Oldx',oldX,'oldy',oldY,'tempSegX',tempSeg.x,'tempSegY',tempSeg.y,'SegX',self.segList[0].x,'SegY',self.segList[0].y)
            
        else:
            self.posDict[self.segList[0].coOrd] = 0
            
        self.segList[0].updatePos(self.dir)
        self.xPos = self.segList[0].getX()
        self.yPos = self.segList[0].getY()
        #print('NewHeadX',self.segList[0].x,'NewHeadY',self.segList[0].y)
        self.coOrd = (self.xPos, self.yPos)
        if self.coOrd in self.posDict and self.posDict[self.coOrd] == 1:
            self.status = SNAKESTAT.DEAD
        else:
            self.posDict[self.coOrd] = 1
        #print(self.posDict)


        
        
    def grow(self,doubleBack):
        #print("Growing....")
        self.segList[0].setType(SEGTYPE.BODY)
        
        self.segList.insert(0,Segment(SEGTYPE.HEAD, RED, self.segList[0].x, self.segList[0].y))
        #self.segList[0].updatePos(self.dir)
        for i in range (0,20):
            self.handleKeyWhenGrow(doubleBack)
        self.updatePos(doubleBack)
        #print("Grown Head X",self.segList[0].x, "Grown Head Y",self.segList[0].y)
        
    
        self.posDict[self.segList[0].coOrd] = 1
        #print(self.posDict)
        #for seg in self.segList:
         #   print("X:",seg.x,"Y:",seg.y)
        
    def handleKeyWhenGrow(self,doubleBack):
        keyPressed = pg.key.get_pressed()
        if keyPressed[pg.K_LEFT] and (doubleBack or not(self.dir == DIR.RIGHT)):
            self.dir = DIR.LEFT
        elif keyPressed[pg.K_UP] and (doubleBack or not(self.dir == DIR.DOWN)):
            self.dir = DIR.UP
        elif keyPressed[pg.K_RIGHT] and (doubleBack or not(self.dir == DIR.LEFT)):
            self.dir = DIR.RIGHT
        elif keyPressed[pg.K_DOWN] and (doubleBack or not(self.dir == DIR.UP)):
            self.dir = DIR.DOWN
            
    def draw(self, surface):
        for seg in self.segList:
            seg.draw(surface)

class Segment:
    def __init__(self,segType,segColour,xPos,yPos):
        # Type = 1 - Head, 2 - Body, 3 - Fruit.
        self.segType = segType
        self.colour = segColour
        self.x = xPos
        self.y = yPos
        self.coOrd = (self.x, self.y)
        
    def setType(self,segType):
        self.segType = segType
        if self.segType == SEGTYPE.HEAD:
            self.colour = RED
        elif self.segType == SEGTYPE.BODY:
                self.colour = GREEN
        elif self.segType == SEGTYPE.FRUIT:
                self.colour = BLUE
        
    def updatePos(self,dir):
        if dir == DIR.LEFT:
            if self.x > 0:
                self.x -= 1
            else:
                self.x = (PLAY_SIZE[0] // PIX_WIDTH) - 1
        elif dir == DIR.UP:
            if self.y > 0:
                self.y -= 1
            else:
                self.y = (PLAY_SIZE[1] // PIX_HEIGHT) - 1
        elif dir == DIR.RIGHT:
            if self.x < (PLAY_SIZE[0] // PIX_WIDTH) - 1:
                self.x += 1
            else:
                self.x = 0
        elif dir == DIR.DOWN:
            if self.y < (PLAY_SIZE[1] // PIX_HEIGHT) - 1:
                self.y += 1
            else:
                self.y = 0

        self.coOrd = (self.x, self.y)

    def draw(self,surface):
        xPos = self.x * PIX_WIDTH
        yPos = self.y * PIX_WIDTH
        self.rect = pg.Rect(self.x*PIX_WIDTH,self.y*PIX_HEIGHT,PIX_WIDTH,PIX_HEIGHT)
        pg.draw.rect(surface,self.colour,self.rect)
        if self.segType == SEGTYPE.HEAD:           # Draw some eyes
            pg.draw.circle(surface,BLACK,(xPos+4,yPos+6),2)
            pg.draw.circle(surface,BLACK,(xPos+16,yPos+6),2)

    def setColour(self,colour):
        self.colour = colour

    def getCoord(self):
        return self.coOrd

    def getX(self):
        return self.x
    def getY(self):
        return self.y

#Main
pg.init()
game = SnakeGame("Snake")
game.doMenu()
pg.quit()
