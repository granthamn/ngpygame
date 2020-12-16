import pygame as pg
import random
import math
from decimal import *

WHITE=(255,255,255)
pg.init()
DS = pg.display.set_mode((500,500))

pg.display.set_caption("Circles!")

space = 0
while space == 0:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                space = 1

for i in range(250,10,-10):
    length = i
    angle = Decimal(0)
    angle_step = Decimal(5)
    colour  = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    while(int(angle) < 256):
        pg.event.get()
        pg.time.Clock().tick(200)
        x = Decimal(length * math.cos(angle))
        y = Decimal(length * math.sin(angle))

        DS.set_at((int(x)+250,int(y)+250),colour)
        angle = angle + angle_step
        pg.display.update()

DS.fill((0,0,0))


length = 50
angle = Decimal(0)
angle_step = Decimal(5)

while angle < 255:
    print(angle)
    pg.time.Clock().tick(10)
    x = angle
    y = Decimal(length * math.sin(math.radians(angle)))
    DS.set_at((int(x),int(y)+250),WHITE)
    angle = angle + angle_step
    pg.display.update()

DS.fill((0,0,0))

for j in range(30):
    pg.event.get()
    colour  = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    cirlen = random.randint(20,250)
    for i in range(10,cirlen):
        angle = 0.0
        step = random.randint(5,50)
        step = step / 100
        length = random.randint(50,350)
        pg.time.Clock().tick(200)
        while (angle < 2 * math.pi):
         
            x = int(i * math.cos(angle))
            y = int(i * math.sin(angle))
            #DS.set_at((x + 250, y+250),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            DS.set_at((x+250,y+250),colour)
            angle = angle + step
            
       
        pg.display.update()

DS.fill((0,0,0))

for j in range(30):
    pg.event.get()
    colour  = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    cirlen = random.randint(20,250)
    for i in range(10,cirlen):
        angle = 0.0
        step = 0.1
        length = random.randint(50,350)
        pg.time.Clock().tick(200)
        while (angle < 2 * math.pi):
        
            x = int(i * math.cos(angle))
            y = int(i * math.sin(angle))
            #DS.set_at((x + 250, y+250),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            DS.set_at((x+250,y+250),colour)
            angle = angle + step
            
       
        pg.display.update()

pg.quit()


