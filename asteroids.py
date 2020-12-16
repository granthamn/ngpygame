import pygame as pg
import time
import math
import random
from AstConsts import *


class spaceObject():
    def __init__(self,xPos,yPos,velocity, objType, width):
        self.xPos = xPos
        self.yPos = yPos
        self.velocity = velocity
        self.objType = objType
        self.velX = 0.0
        self.velY = 0.0
        self.incVel = False
        self.decVel = False
        self.width = width


class Bullet(spaceObject):
    def __init__(self,xPos,yPos,velocity,objType,width,angle):
        super().__init__(xPos,yPos,velocity,objType,width)
        self.angle = angle

    def draw(self, canvas):


        bullRect = pg.Rect(self.xPos, self.yPos, self.width * PIXSIZE, self.width * PIXSIZE)
        pg.draw.rect(canvas, WHITE, bullRect)

    def move(self, elapsed, objList):
        self.velX = self.velocity * math.sin(math.radians(self.angle))
        self.velY = self.velocity * math.cos(math.radians(self.angle))
        self.yPos -= self.velY * elapsed
        self.xPos += self.velX * elapsed
        self.xPos %= WIDTH + self.width
        self.yPos %= HEIGHT + self.width

class Ship(spaceObject):
    def __init__(self, xPos, yPos, velocity, objType, width):
        super().__init__(xPos, yPos, velocity, objType, width)
        self.angle = 0
        self.firing = False

    def draw(self,canvas):

        #pointList = [(self.xPos,self.yPos), (self.xPos+(self.width / 2), self.yPos+self.width), (self.xPos-(self.width /2),self.yPos+(self.width))]
        pointList = [(-self.width / 2 , self.width), (0.0, -self.width), (self.width / 2, self.width)]
        for pc, point in enumerate(pointList):
            px = point[0] * math.cos(math.radians(self.angle)) - point[1] * math.sin(math.radians(self.angle))
            py = point[0] * math.sin(math.radians(self.angle)) + point[1] * math.cos(math.radians(self.angle))
            px += self.xPos
            py += self.yPos
            pointList[pc] = (px,py)

        #pointList = [(newX, newY), (newX1, newY1), (newX2, newY2)]
        pg.draw.lines(canvas,WHITE,True,pointList)

    def move(self,elapsed, objList):

        if self.decVel:
            self.velocity -= 0.1
            if self.velocity < 0:
                self.velocity = 0
        elif self.incVel:
            if self.velocity == 0:
                self.velocity = 1.0
            else:
                self.velocity += VEL_INC
            if self.velocity > MAX_VEL:
                self.velocity = MAX_VEL

        self.velX = self.velocity * math.sin(math.radians(self.angle))
        self.velY = self.velocity * math.cos(math.radians(self.angle))

        self.yPos -= self.velY * elapsed

        self.xPos += self.velX * elapsed

        self.xPos %= WIDTH + self.width
        self.yPos %= HEIGHT + self.width

class Rock(spaceObject):
    def __init__(self, xPos, yPos, velocity, objType, width):
        super().__init__(xPos, yPos, velocity, objType, width)
        randDeg = random.randint(0, 359)
        randRad = (math.pi / 180) * randDeg
        self.angle = randRad

    def draw(self, canvas):
        rockRect = pg.Rect(self.xPos, self.yPos, self.width * PIXSIZE, self.width * PIXSIZE)
        pg.draw.rect(canvas,RED,rockRect)

    def move(self,elapsed, objList):
        self.velX = self.velocity * math.sin(self.angle)
        self.velY = self.velocity * math.cos(self.angle)
        self.yPos -= self.velY * elapsed
        self.xPos += self.velX * elapsed
        self.xPos %= WIDTH + self.width
        self.yPos %= HEIGHT + self.width

class Asteroids:
    def __init__(self,caption):
        self.screen = pg.display.set_mode(WINSIZE)
        self.DS = pg.Surface(WINSIZE)
        self.quit = False
        self.currTime = None
        self.nextTime = None
        self.elapsed = None
        self.objList = []
        self.incShipVol = False
        self.decShipVol = False
        self.thruster = None
        self.numBullets = 0
        self.theShip = Ship((WIDTH / 2) - (SHIPWIDTH / 2),(HEIGHT / 2) - SHIPWIDTH,0.0,"Ship", SHIPWIDTH)
        self.objList.append(self.theShip)
        self.setUpRocks()
        self.initMusic()


    def initMusic(self):
        self.thruster = pg.mixer.Sound('music/thrust.wav')
        self.shooter = pg.mixer.Sound('music/pew.wav')
        self.hit = pg.mixer.Sound('music/kaboom.wav')

    def setUpRocks(self):
        for i in range(0,MAX_ROIDS):
            x = random.randint(0,WIDTH - 1)
            y = random.randint(0,HEIGHT - 1)
            vel = random.randrange(10,MAX_VEL,5)
            width = random.randint(2,6)
            self.objList.append(Rock(x, y, vel, "Rock", width))


    def checkKeys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.thruster.play()
            if self.theShip.velocity < MAX_VEL:
                self.theShip.decVel = False
                self.theShip.incVel = True
        elif self.theShip.velocity > 0:
            self.thruster.stop()
            self.theShip.decVel = True
            self.theShip.incVel = False
        else:
            self.theShip.decVel = False
            self.theShip.incVel = False

        # TO DO -  convert rocks angle to degrees.
        if keys[pg.K_LEFT]:
            if self.theShip.velocity == 0:
                self.theShip.angle -= 100 * self.elapsed
            else:
                self.theShip.angle -= self.theShip.velocity * self.elapsed
            self.theShip.angle %= 359

        if keys[pg.K_RIGHT]:
            if self.theShip.velocity == 0:
                self.theShip.angle += 100 * self.elapsed
            else:
                self.theShip.angle += self.theShip.velocity * self.elapsed
            self.theShip.angle %= 359

        if keys[pg.K_SPACE]:
            if self.theShip.firing == False and self.numBullets < MAX_BULLS:
                self.theShip.firing = True
                self.shooter.play()
                self.numBullets += 1

                bullX = self.theShip.velocity * math.sin(math.radians(self.theShip.angle))
                bullY = self.theShip.velocity * math.cos(math.radians(self.theShip.angle))

                bullX += self.theShip.xPos
                bullY -= self.theShip.yPos

                #self.objList.append(Bullet(bullX, bullY, BULLET_VEL, "Bullet", 1,self.theShip.angle))
                self.objList.append(Bullet(self.theShip.xPos, self.theShip.yPos, BULLET_VEL, "Bullet", 1, self.theShip.angle))

        else:
            self.theShip.firing = False



    def moveObjects(self):
        for obj in self.objList:
            obj.move(self.elapsed,self.objList)


        # print(self.theShip.xPos, self.theShip.yPos)

        # self.theShip.yPos -= int(self.theShip.velocity * self.elapsed)

    def clearScreen(self):
        self.DS.fill(BLACK)

    def drawObjects(self):
        for obj in self.objList:
            obj.draw(self.DS)

    def checkBulletCollisions(self):
        for obj in self.objList:
            if obj.objType == "Bullet":
                bullX = obj.xPos + obj.width * PIXSIZE
                bullY = obj.yPos + obj.width * PIXSIZE
                for rock in self.objList:
                    if rock.objType == "Rock":
                        if bullX  > rock.xPos and bullX <= rock.xPos + (rock.width * PIXSIZE):
                            if bullY > rock.yPos and bullY <= rock.yPos + (rock.width * PIXSIZE):
                                self.hit.play()
                                self.objList.remove(obj)
                                self.numBullets -= 1

    def mainLoop(self):
        space = 0
        # Little loop to show starting point for preset patterns.
        while space == 0:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        space = 1

        self.currTime = time.monotonic()
        while not self.quit:
            # Timing
            self.nextTime = time.monotonic()
            self.elapsed = self.nextTime - self.currTime
            self.currTime = self.nextTime

            # Inputs
            for ev in pg.event.get():
                if ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE:
                    self.quit = True
            self.checkKeys()

            # Logic
            if self.numBullets:
                self.checkBulletCollisions()
            self.moveObjects()



            # Display
            self.clearScreen()
            self.drawObjects()

            self.screen.blit(self.DS, (0, 0))
            pg.display.update()

pg.mixer.pre_init(44100, -16, 2, 512)
pg.mixer.init()
pg.init()
game = Asteroids("Asteroids")
game.mainLoop()
pg.quit()
