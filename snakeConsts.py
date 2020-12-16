from enum import Enum
# Constants
PIX_HEIGHT, PIX_WIDTH = 20,20
WINSIZE=(500,500)
PLAY_SIZE=(400,400)
GREY=(100,100,100)
RED=(150,20,20)
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(20,50,250)
GREEN=(0,200,75)
BROWN=(200,100,0)
BRIGHTRED=(255,0,0)
#Enums

class DIR(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4

class SEGTYPE(Enum):
    HEAD = 1
    BODY = 2
    FRUIT = 3

class SNAKESTAT(Enum):
    ALIVE = 1
    DEAD = 2

class MODE(Enum):
    EASY = 0
    HARD = 1

class SPEED(Enum):
    NORMAL = 100
    FAST = 70
