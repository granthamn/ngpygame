import pygame as pg
import random
from mazeconsts import *
from collections import deque

class Cell:
    def __init__(self,xPos,yPos,stats):
        self.x = xPos
        self.y = yPos
        #stats = (Visited,PathN,PathE,PathS,Pathw)
        self.stats = stats

    def getVisited(self):
        return self.stats[0]
    
    def setVisited(self):
        self.stats = (1,) + self.stats[1:]

    def setPath(self,pathElem):
        self.stats = self.stats[:pathElem] + (1,) + self.stats[pathElem+1:]
        #print(self.stats)
        #print(self.x,self.y)
    def getYPos(self):
        return self.y

    def getXPos(self):
        return self.x

    def getEastPath(self):
        return self.stats[2]

    def getSouthPath(self):
        return self.stats[3]
    def getStats(self):
        return self.stats

                                  
class Maze:
    def __init__(self,caption):
        """ Maze creator using stack and back-tracking"""
        self.totSquares = (PLAY_WIDTH * PLAY_HEIGHT) # How many maze cells to visit in total
        self.visitCount = 0
        self.stack = deque()                         # To hold current path
        #Hold maze as big fuck off 1d list. Below seems right dimensions wise
        self.maze = [Cell(x%PLAY_WIDTH,x//PLAY_WIDTH,(0,0,0,0,0)) for x in range(self.totSquares)]
       
        self.DS  = pg.display.set_mode(WINSIZE)
        self.clock = pg.time.Clock()
        pg.display.set_caption(caption)
        self.quit = False
        #print(len(self.maze))

    def setup(self):
        startX = random.randint(0,PLAY_WIDTH-1)
        startY = random.randint(0,PLAY_HEIGHT-1)
       
        self.stack.append(Cell(startX,startY,(1,0,0,0,0)))
        self.maze[startY*PLAY_WIDTH+startX].setVisited()
        #print("Starting at: ",startX,startY)

    def getIndex(self,px,py):
        # Hide the ugly index calc into the maze array here
        return (self.stack[-1].getYPos()+py) * PLAY_WIDTH + (self.stack[-1].getXPos()+px)
           
    def main(self):
        #Setup
        self.setup()
        space = 0       
        while not self.quit and self.visitCount < self.totSquares - 1:
             
            #Timings - 20fps
            self.clock.tick(100)
            
            # Inputs
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True
            # Logic
            neighbours = []
            
            #Check neighbours not already visited.
            if self.stack[-1].getYPos() > 0 and self.maze[self.getIndex(0,-1)].getVisited() == False:
                neighbours.append(0)
                #print("Has North")
            if self.stack[-1].getXPos() < PLAY_WIDTH - 1 and self.maze[self.getIndex(1,0)].getVisited() == False:
                neighbours.append(1)
                #print("Has East")
            if self.stack[-1].getYPos() < PLAY_HEIGHT - 1 and self.maze[self.getIndex(0,1)].getVisited() == False:
                neighbours.append(2)
                #print("Has South")
            if self.stack[-1].getXPos() > 0 and self.maze[self.getIndex(-1,0)].getVisited() == False:
                neighbours.append(3)
                #print("Has West")

            # Pick a random neighbour
            if len(neighbours):
                nextCell = neighbours[random.randrange(len(neighbours))]
                if nextCell == 0:   # North
                   # print("Chose North")
                    nextX = 0
                    nextY = -1
                    nextpathElem = 3    # Cell is north so has a path south etc.
                    pathElem = 1
                elif nextCell == 1: # East
                    #print("Chose East")
                    nextX = 1
                    nextY = 0
                    nextpathElem = 4
                    pathElem = 2
                elif nextCell == 2: # South
                    #print("Chose South")
                    nextX = 0
                    nextY = 1
                    nextpathElem = 1
                    pathElem = 3
                else:               # West
                    #print("Chose West")
                    nextX = -1
                    nextY = 0
                    nextpathElem = 2
                    pathElem = 4
                #print("Next coord diff:",nextX,nextY)
                #print("Next Coord:",self.getIndex(nextX,nextY))
                self.maze[self.getIndex(nextX,nextY)].setVisited()
                self.visitCount+=1
                self.maze[self.getIndex(nextX,nextY)].setPath(nextpathElem)
                self.maze[self.getIndex(0,0)].setPath(pathElem)
                self.stack.append(self.maze[self.getIndex(nextX,nextY)])

            else:
                self.stack.pop()
            
            # Drawing - draw display buffer
            self.DS.fill(BLACK)
            for y in range(PLAY_HEIGHT):
                for x in range(PLAY_WIDTH):
                    if self.maze[y*PLAY_WIDTH+x].getVisited() == 1:
                        self.cellColour = WHITE
                    else:
                        self.cellColour = BLUE
                    cellLocX = x*(PIX_SIZE+WALLWIDTH)
                    cellLocY = y*(PIX_SIZE+WALLWIDTH)
                    self.cellRect = pg.Rect(cellLocX,cellLocY,PIX_SIZE,PIX_SIZE)
                    
                    pg.draw.rect(self.DS,self.cellColour,self.cellRect)
                    if self.maze[y*PLAY_WIDTH+x].getEastPath():
                        self.cellRect = pg.Rect(cellLocX+PIX_SIZE,cellLocY,WALLWIDTH,PIX_SIZE)
                        pg.draw.rect(self.DS,self.cellColour,self.cellRect)
                    if self.maze[y*PLAY_WIDTH+x].getSouthPath():
                        self.cellRect = pg.Rect(cellLocX,cellLocY+PIX_SIZE,PIX_SIZE,WALLWIDTH)
                        pg.draw.rect(self.DS,self.cellColour,self.cellRect)
                    headCell = self.stack[-1]
                    #print(self.stack[-1].getXPos(),self.stack[-1].getYPos())
                    self.cellRect = pg.Rect(headCell.getXPos()*(PIX_SIZE+WALLWIDTH),headCell.getYPos()*(PIX_SIZE+WALLWIDTH),PIX_SIZE,PIX_SIZE)
                    pg.draw.rect(self.DS,GREEN,self.cellRect)
                    startCell = self.stack[0]
                    self.cellRect = pg.Rect(startCell.getXPos()*(PIX_SIZE+WALLWIDTH),startCell.getYPos()*(PIX_SIZE+WALLWIDTH),PIX_SIZE,PIX_SIZE)
                    pg.draw.rect(self.DS,RED,self.cellRect)
            pg.display.update()
             # Little loop to show starting point.
            while space == 0:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            space = 1
#Main
pg.init()
theMaze = Maze("Maze Creator")
theMaze.main()
pg.quit()
