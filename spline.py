import pygame as pg
import random
from splineConsts import *
import cProfile
import time
import numpy as np



class Point:
    def __init__(self,x,y,colour):
        self.x = x
        self.y = y
        self.label = ""
        self.colour = colour
        
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setLabel(self,label,font):
        self.label = label
        self.text = font.render(self.label,True,WHITE)

    def getLabel(self):
        return self.label

    def getText(self):
        return self.text

    def getColour(self):
        return self.colour

    def setColour(self,colour):
        self.colour = colour

    def moveX(self,dist):
        self.x += dist

    def moveY(self,dist):
        self.y += dist

    def draw(self,surf):
        pointRect = pg.Rect(int(self.x),int(self.y),PIX_SIZE,PIX_SIZE)
        pg.draw.rect(surf,WHITE,pointRect)
        #print("X",self.x,"Y",self.y)


class Spline:
    def __init__(self,pointList,font):
        self.pointList = pointList
        for c,v in enumerate(pointList):
            v.setLabel(str(c),font)
        self.selectedPoint = 0
        self.pointList[self.selectedPoint].setColour(GREEN)

    def draw(self,surf):

        for t in np.arange(0,len(self.pointList) -3, 0.01):
           
            posPoint = self.getPoint(t)
            posPoint.draw(surf)
        
        for point in self.pointList:
            pointRect = pg.Rect(int(point.getX())-PIX_SIZE,int(point.getY())-PIX_SIZE,3*PIX_SIZE,3*PIX_SIZE)
            #print("CP",point.getLabel(), point.getX(), ",", point.getY())
            pg.draw.rect(surf,point.getColour(),pointRect)
            surf.blit(point.getText(),(int(point.getX()),int(point.getY())))

       
        

    def checkMouse(self,x,y):
        for point in self.pointList:
            if x > point.getX()-PIX_SIZE and x < point.getX()+(3*PIX_SIZE):
                if y > point.getY()-PIX_SIZE and y < point.getY()+(3*PIX_SIZE):
                    point.setColour(GREEN)
                    if self.pointList[self.selectedPoint].getColour() == GREEN and self.selectedPoint != int(point.getLabel()):
                        self.pointList[self.selectedPoint].setColour(RED)
                    self.selectedPoint = int(point.getLabel())
                    
    def moveSelectedPoint(self,elapsed,direc,factor):
        moveBy = (factor * 80) * elapsed
        if direc == 0:
            self.pointList[self.selectedPoint].moveX(moveBy)
        else:
             self.pointList[self.selectedPoint].moveY(moveBy)

    def setSelectedPoint(self):
        self.pointList[self.selectedPoint].setColour(RED)
        if self.selectedPoint == len(self.pointList) - 1:
            self.selectedPoint = 0
        else:
            self.selectedPoint += 1
        self.pointList[self.selectedPoint].setColour(GREEN)

    def getPoint(self,t):
        p1 = int(t) + 1
        p2 = p1 + 1
        p3 = p2 + 1
        p0 = p1 - 1

        t = t - int(t)
        
        tt = t * t
        ttt = tt * t

        q1 = -ttt + 2.0*tt - t
        q2 = 3.0 * ttt - 5.0 * tt + 2.0
        q3 = -3.0 * ttt + 4.0 * tt + t
        q4 = ttt - tt
        #print("1",q1,"2",q2,"3",q3,"q4",q4)
        tx = 0.5 * (self.pointList[p0].getX() * q1 + self.pointList[p1].getX() * q2 + self.pointList[p2].getX() * q3 + self.pointList[p3].getX() * q4)
        ty = 0.5 * (self.pointList[p0].getY() * q1 + self.pointList[p1].getY() * q2 + self.pointList[p2].getY() * q3 + self.pointList[p3].getY() * q4) 
        
        return(Point(tx,ty,WHITE))
        
#Splines
class Splines:
    def __init__(self,caption):
        self.screen  = pg.display.set_mode(WINSIZE) 
        self.DS = pg.Surface(WINSIZE)
        self.clock = pg.time.Clock()
        pg.display.set_caption(caption)
        self.quit = False
        self.labelFont = pg.font.SysFont("Arial",10,True)
        listOfPoints = [Point(x,328,RED) for x in range(140,1020,80)]
        self.theSpline = Spline(listOfPoints,self.labelFont)
        #self.theSpline = Spline([Point(120,328,RED),Point(360,328,RED),Point(600,328,RED),Point(840,328,RED)],self.labelFont)

    def checkMouseDown(self):
        md = pg.mouse.get_pressed()
        if md[0] == 1:
            mPos = pg.mouse.get_pos()
            mx = mPos[0]
            my = mPos[1]
            self.theSpline.checkMouse(mx,my)

    def checkKeyPress(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.theSpline.moveSelectedPoint(self.elapsed,0,-1)
        if keys[pg.K_RIGHT]:
            self.theSpline.moveSelectedPoint(self.elapsed,0,1)
        if keys[pg.K_UP]:
            self.theSpline.moveSelectedPoint(self.elapsed,1,-1)
        if keys[pg.K_DOWN]:
            self.theSpline.moveSelectedPoint(self.elapsed,1,1)
            
    def mainLoop(self):
       
        tick = time.monotonic()
        while not self.quit:
            #Timings 
            nextTick = time.monotonic()
            self.elapsed = nextTick - tick
            tick = nextTick


            # Inputs
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.theSpline.setSelectedPoint()
            self.checkKeyPress()        
            self.checkMouseDown()


            # Logic

            # Drawing
            self.DS.fill(BLACK)
            self.theSpline.draw(self.DS)
            self.screen.blit(self.DS,(0,0))            
            pg.display.flip()

        
      
           
          
            
#Main
pg.init()
sp = Splines("Splines")
sp.mainLoop()
pg.quit()
