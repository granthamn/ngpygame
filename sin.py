import pygame as pg
import math
from decimal import *


WHITE=(255,255,255)
pg.init()
DS = pg.display.set_mode((500,500))


myText = "Circle plotted using vector (angle and length"
myText2 = "Circle plotted using radians"
myText3 = "Plot of SIN and COS functions"
myText4 = "Using sin and cos to make an accelerating,rotating object"
myText5 = "Object orbiting another moving object"
myfont = pg.font.SysFont("Arial",14,True)

text = myfont.render(myText,True,WHITE)
DS.blit(text,(100,200))
pg.display.update()
space = 0
while space == 0:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                space = 1
space = 0
DS.fill((0,0,0))

length = 50
angle = 0
angle_step = 0.1

while angle < 2 * math.pi:
    pg.event.get()
    pg.time.Clock().tick(50)
    x = length * math.cos(angle)
    y = length * math.sin(angle)
    DS.set_at((int(x)+250,int(y)+250),WHITE)
    angle = angle + angle_step
    pg.display.update()

DS.fill((0,0,0))

text = myfont.render(myText2,True,WHITE)
DS.blit(text,(100,200))
pg.display.update()
space = 0
while space == 0:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                space = 1
space = 0
DS.fill((0,0,0))


angle = Decimal(0)
angle_step = Decimal(5)

while (angle < 256):
    pg.event.get()
    pg.time.Clock().tick(50)
    x = length * math.cos(angle)
    y = length * math.sin(angle)
    DS.set_at((int(x)+250,int(y)+250),WHITE)
 
    angle = angle + angle_step
    pg.display.update()

DS.fill((0,0,0))

text = myfont.render(myText3,True,WHITE)
DS.blit(text,(100,200))
pg.display.update()
space = 0
while space == 0:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                space = 1
space = 0
DS.fill((0,0,0))

angle = Decimal(0)
angle_step = Decimal(5)

while (angle < 360):
    pg.event.get()
    pg.time.Clock().tick(50)
    x = angle
    y = length * math.cos(math.radians(angle))
    yy = length * math.sin(math.radians(angle))
    
    DS.set_at((int(x),int(y)+250),WHITE)
    DS.set_at((int(x),int(yy)+250),(255,0,0))
    angle = angle + angle_step
    pg.display.update()

DS.fill((0,0,0))


text = myfont.render(myText4,True,WHITE)
DS.blit(text,(100,200))
pg.display.update()
space = 0
while space == 0:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                space = 1
space = 0
DS.fill((0,0,0))


angle = 0.0
length = 0.0
x,y = 250,250
vel_x, vel_y = 0.0, 0.0
quitGame = False
bullets = []
while not quitGame:
    pg.time.Clock().tick(50)
    DS.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and length < 4:
                length = length + 0.1
            elif event.key == pg.K_DOWN and length > 0:
                length = length - 0.1
            elif event.key == pg.K_LEFT:
                angle = (angle - 0.5)
            elif event.key == pg.K_RIGHT:
                angle = angle + 0.5
            elif event.key == pg.K_ESCAPE:
                quitGame = True
           
    vel_x = length * math.cos(angle)
    vel_y = length * math.sin(angle)
   
    x = x + vel_x
    y = y + vel_y
    pg.draw.circle(DS,WHITE,(int(x),int(y)),10)
    pg.draw.line(DS,(255,0,0),(int(x),int(y)),(int(x+9 * math.cos(angle)),int(y+9 * math.sin(angle))))

    pg.display.update()

space = 0
DS.fill((0,0,0))
pg.display.update()


text = myfont.render(myText5,True,WHITE)
DS.blit(text,(100,200))
pg.display.update()
while space == 0:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                space = 1

DS.fill((0,0,0))
x = 0
y = 0

len_x = 50
len_y = 50
quitGame = False
angle = 0
angle_step = 0.1
circ_cent_X = 250
circ_cent_Y = 250

while not quitGame:
    pg.time.Clock().tick(100)
    DS.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                quitGame = True
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT] and circ_cent_X > 50:
        circ_cent_X -= 0.75
    if keys[pg.K_RIGHT] and circ_cent_X < 450:
        circ_cent_X += 0.75
    if keys[pg.K_UP] and circ_cent_Y > 50:
        circ_cent_Y -= 0.75
    if keys[pg.K_DOWN] and circ_cent_Y < 450:
        circ_cent_Y += 0.75
                
    x = len_x * math.cos(angle)
    y = len_y * math.sin(angle)

    pg.draw.circle(DS,(155,20,50),(int(circ_cent_X),int(circ_cent_Y)),10)
    DS.set_at((int(x)+int(circ_cent_X),int(y)+int(circ_cent_Y)),WHITE)
    if angle < 256:
        angle = angle + angle_step
    else:
        angle = 0
    pg.display.update()
pg.quit()
