import pygame as pg
import math
import time

WINSIZE = (960,480)
PIXSIZE = 8
PLAY_WIDTH = WINSIZE[0] // PIXSIZE
PLAY_HEIGHT = WINSIZE[1] // PIXSIZE

class Player:
    def __init__(self):
        self.x = 10.0
        self.y = 6.0
        self.angle = 255.0
        self.fov = math.pi / 4.0
        
    def getFov(self):
        return self.fov
    def getAngle(self):
        return self.angle
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setAngle(self,angle):
        self.angle += angle
    def setX(self,newX):
        self.x = newX
    def setY(self,newY):
        self.y = newY

class Map:
    def __init__(self,w,h):
        self.width = w
        self.font = pg.font.SysFont("Arial",12,True)
        self.height = h
        self.mapList = [["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
                        ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                        ["#"," ","" ," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                        ["#"," ","#"," "," "," "," "," "," "," ","#","#"," "," "," ","#"],
                        ["#"," ","#"," "," "," "," "," "," "," ","#","#"," "," "," ","#"],
                        ["#"," ","#"," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                        ["#"," ","#"," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                        ["#"," ","#"," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                        ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                        ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                        ["#"," "," "," "," "," ","#"," "," "," "," "," "," "," "," ","#"],
                        ["#"," "," "," "," "," ","#","#"," "," "," "," "," "," "," ","#"],
                        ["#"," "," "," "," "," ","#","#","#"," "," "," "," "," "," ","#"],
                        ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                        ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
                        ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]
                        
        
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getMapCoord(self,y,x):
        return self.mapList[y][x]
    def draw(self,surf,y,x):
        for px in range(len(self.mapList)):
            for py in range(len(self.mapList[px])):
                if self.mapList[px][py] == "#":
                    col = (255,255,255)
                else:
                    col = (0,0,0)
                if x == py and y == px:
                    col = (255,0,0)
                    
                mapRect = pg.Rect(0+(PIXSIZE / 2)*px,0+(PIXSIZE / 2) * py,PIXSIZE / 2,PIXSIZE / 2)
                pg.draw.rect(surf,col,mapRect)

            


class FPSGame:
    def __init__(self,caption):
        self.quitGame = False
        self.screen = pg.display.set_mode((WINSIZE))
        self.DS = pg.Surface(WINSIZE)
        pg.display.set_caption(caption)
        self.player = Player()
        self.map = Map(16,16)
        self.theClock = pg.time.Clock()
        self.shader = 10

    def draw(self,angle,fov):
        
        for x in range(PLAY_WIDTH):
            isBoundary = False
            self.rayAngle = (angle - fov / 2.0) + (x / PLAY_WIDTH) * fov
            self.distanceToWall = 0.0
            self.hitWall = False

            self.viewX = math.sin(self.rayAngle)
            self.viewY = math.cos(self.rayAngle)

            while self.hitWall == False and self.distanceToWall < 16:
                self.distanceToWall += 0.1
                self.testX = int(self.player.getX() + self.viewX * self.distanceToWall)
                self.testY = int(self.player.getY() + self.viewY * self.distanceToWall)

                if self.testX < 0 or self.testY >= self.map.getWidth() or self.testY < 0 or self.testY >= self.map.getHeight():
                    self.hitWall = True
                    self.distanceToWall = 16
                else:
                    
                    vecList = []
                    if self.map.mapList[self.testY][self.testX] == "#":
                        self.hitWall = True
                        for tx in range(0,2):
                            for ty in range(0,2):
                                vy = float(self.testY) + ty - self.player.getY()
                                vx = float(self.testX) + tx - self.player.getX()
                                mag = math.sqrt(vx*vx + vy*vy)
                                dot = (self.viewX * vx / mag) + (self.viewY * vy / mag)
                                vecList.append((mag,dot))
                                vecList.sort(key=lambda dx: dx[0])

                        bounds = 0.01
                        #print(vecList[0][1])
                        if math.acos(vecList[0][1]) < bounds:
                            isBoundary = True
                        if math.acos(vecList[1][1]) < bounds:
                            isBoundary = True
                       
            self.ceiling = float(PLAY_HEIGHT / 2.0) - PLAY_HEIGHT / float(self.distanceToWall)
            self.floor = PLAY_HEIGHT - self.ceiling
            if self.distanceToWall <= 16.0 / 4.0:
                self.shader = 0
            elif self.distanceToWall < 16.0 / 3.5:
                self.shader = 40
            elif self.distanceToWall < 16.0 / 3.0:
                self.shader = 80
            elif self.distanceToWall < 16.0 / 2.5:
                self.shader = 120
            elif self.distanceToWall < 16.0 / 2.0:
                self.shader = 160
            elif self.distanceToWall < 16.0:
                self.shader = 200
            if isBoundary == True:
                self.shader = 255
            for y in range(PLAY_HEIGHT):
                if y < self.ceiling:
                    self.wallRect = pg.Rect(x * PIXSIZE,y*PIXSIZE,PIXSIZE,PIXSIZE)
                    pg.draw.rect(self.DS,(0,60,200),self.wallRect)
                    #do nowt
                elif y > self.ceiling and y <= self.floor:
                    self.wallRect = pg.Rect(x * PIXSIZE,y*PIXSIZE,PIXSIZE,PIXSIZE)
                    pg.draw.rect(self.DS,(255-self.shader,255-self.shader,255-self.shader),self.wallRect)
                elif y >= self.floor:
                    fShad = 1.0 - (float(y - PLAY_HEIGHT / 2.0) / float(PLAY_HEIGHT / 2.0))
                    
                    if fShad < 0.25:
                        self.shader = 110
                    elif fShad < 0.5:
                        self.shader = 90
                    elif fShad < 0.75:
                        self.shader = 70
                    else:
                        self.shader = 40
                    self.wallRect = pg.Rect(x * PIXSIZE,y*PIXSIZE,PIXSIZE,PIXSIZE)
                    pg.draw.rect(self.DS,(self.shader,self.shader,self.shader),self.wallRect)
    def main(self):
        self.timer = time.monotonic()
        while not self.quitGame:
            self.timer2 = time.monotonic()
            elapsed = self.timer2 - self.timer
            self.timer = self.timer2
            
            tempAngle = self.player.getAngle()
            tempX = self.player.getX()
            tempY = self.player.getY()
            # Timing
            #self.theClock.tick(100)# 30fps
            # Input
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quitGame = True
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.player.setAngle(-0.5 * elapsed)
            if keys[pg.K_RIGHT]:
                self.player.setAngle(0.5 * elapsed)
            if keys[pg.K_UP]:
                newX = tempX + math.sin(tempAngle) * 5.0 * elapsed
                newY = tempY + math.cos(tempAngle) * 5.0 * elapsed
                #print("UP",int(self.player.getX()),int(self.player.getY()))
                if self.map.getMapCoord(int(newY),int(newX)) == "#":
                    newX = tempX - math.sin(tempAngle) * 5.0 * elapsed
                    newY = tempY - math.cos(tempAngle) * 5.0 * elapsed
                    #print("NEXT",int(newX),int(newY))
                self.player.setX(newX)
                self.player.setY(newY)
            if keys[pg.K_DOWN]:
                newX = tempX - math.sin(tempAngle) * 5.0 * elapsed
                newY = tempY - math.cos(tempAngle) * 5.0 * elapsed
                #print("DOWN",int(self.player.getX()),int(self.player.getY()))
                if self.map.getMapCoord(int(newY),int(newX)) == "#":
                    newX = tempX + math.sin(tempAngle) * 5.0 * elapsed
                    newY = tempY + math.cos(tempAngle) * 5.0 * elapsed
                    #print("NEXT",int(newX),int(newY))
                self.player.setX(newX)
                self.player.setY(newY)
            # Strafe Left
            if keys[pg.K_z]:
                newX = tempX - math.cos(tempAngle) * 5.0 * elapsed
                newY = tempY + math.sin(tempAngle) * 5.0 * elapsed
                #print("UP",int(self.player.getX()),int(self.player.getY()))
                if self.map.getMapCoord(int(newY),int(newX)) == "#":
                    newX = tempX + math.cos(tempAngle) * 5.0 * elapsed
                    newY = tempY - math.sin(tempAngle) * 5.0 * elapsed
                    #print("NEXT",int(newX),int(newY))
                self.player.setX(newX)
                self.player.setY(newY)
            # Strafe Right
            if keys[pg.K_x]:
                newX = tempX + math.cos(tempAngle) * 5.0 * elapsed
                newY = tempY - math.sin(tempAngle) * 5.0 * elapsed
                #print("UP",int(self.player.getX()),int(self.player.getY()))
                if self.map.getMapCoord(int(newY),int(newX)) == "#":
                    newX = tempX - math.cos(tempAngle) * 5.0 * elapsed
                    newY = tempY + math.sin(tempAngle) * 5.0 * elapsed
                    #print("NEXT",int(newX),int(newY))
                self.player.setX(newX)
                self.player.setY(newY)
            # Logic
            
            # Rendering
            self.DS.fill((0,0,0))
            self.draw(self.player.getAngle(),self.player.getFov())
            self.map.draw(self.DS,int(self.player.getY()),int(self.player.getX()))
            self.screen.blit(self.DS,(0,0))
            pg.display.flip()
#Main
pg.init()
pg.mixer.init()
pg.mixer.music.load('music/w3d.mp3')
pg.mixer.music.play()
fpsGame = FPSGame("FPSMaze")
fpsGame.main()
pg.quit()
