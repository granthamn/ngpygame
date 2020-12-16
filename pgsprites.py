import pygame as pg

pg.init()
screen = pg.display.set_mode((400,400))
pg.display.set_caption("Pg Sprites")

bkImg = pg.image.load("img/vgbak.png").convert()
bkImg = pg.transform.scale(bkImg,(400,400))
bkImg.set_colorkey((255,255,255))
img = pg.image.load("img/mm.png").convert()
imcolkey = img.get_at((0,0))
img.set_colorkey((255,255,255))
loc = pg.math.Vector2(96,96)
sprites = []
clock = pg.time.Clock()

spriteCounter = 0
#1) pg.Rect of pos/size of sprite
#2) surface of rect size
#3) Blit image to surgace
#4) Set colour key
#5) Append to array of images
for i in range(0,920,184):
    #for j in range(0,390,195):
    sprite = pg.Surface([184,195]).convert()
    sprite.blit(img, (0,0),(i,195, 184,195))
    sprite.set_colorkey((0,0,0))
    sprites.append(sprite)

    


screen.blit(bkImg,(0,0))




space = 0


while space == 0:
    clock.tick(10)
    if spriteCounter == len(sprites):
        spriteCounter = 0
    screen.blit(sprites[spriteCounter],(160,140))
    spriteCounter += 1
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                space = 1
        
    pg.display.update()
    
pg.quit()
