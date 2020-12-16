import pygame as pg

pg.init()
screen = pg.display.set_mode((500,500))
pg.display.set_caption("Pygame Basics")

x = 100
y = 100.0
width = 40
height = 40
vel = 5
isJumping = False
jumpCounter = 10

run = True

while run:
    pg.time.Clock().tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > 0: 
        x = x - vel
    if keys[pg.K_RIGHT] and x < screen.get_width() - width:
        x = x + vel
    if not isJumping:
        if keys[pg.K_UP] and y > 0:
            y = y - vel
        if keys[pg.K_DOWN] and y < screen.get_height() - height:
            y = y + vel
        if keys[pg.K_SPACE]:
            isJumping = True
    else:
        if jumpCounter >= -10:
            neg = 1
            if jumpCounter < 0:
               neg = -1
            y -= int((jumpCounter ** 2) * 0.5 * neg)
            jumpCounter -= 1
            print(y)
            print(jumpCounter)
            print(int((jumpCounter **2) * 0.5 * neg))
        else:
            isJumping = False
            jumpCounter = 10
        
    screen.fill((0,0,0))
    pg.draw.rect(screen,(255,0,0),(x,y,width,height))
    pg.display.update()
    
pg.quit()
