import pygame as pg
import math
from decimal import *


class Ship:
    def __init(self,vecVel,xPos,yPos):
        self.vecVel = pg.math.Vector2(0,0)
        self.xPos = xPos
        self.yPos = yPos
        












#Main
pg.init()
shipGame = ShipGame("Space")
shipGame.main()
pg.quit()
