import pygame as pg
import random
import time
import string


WHITE=(255,255,255)
BLACK=(0,0,0)
WINSIZE=(1200,960)
FONTSIZE=12
GREEN=(0,130,0)
DARKGREEN=(0,60,0)
LIGHTGREEN=(0,230,0)
WHITEGREEN=(220,255,220)
WHITISHGREEN=(100 ,220,100)


class MatrixRain:
    def __init__(self,caption):
        self.screen = pg.display.set_mode(WINSIZE)
        self.DS = pg.Surface(WINSIZE)
        
        self.theClock = pg.time.Clock()
        self.quit = False
        self.streamList = []

        self.maxStreams = 200

        for n in range(0,self.maxStreams):
            ranLen = random.randint(18,35)
            ranString  = ''.join(random.choices(string.ascii_uppercase + string.digits + string.punctuation, k=ranLen))
            #stream = self.prepareTextStream("E3FX9%O!PQR$TU?VT@KZ12SK37#89N")
            stream = self.prepareTextStream(ranString)
            stream.xPos = n * FONTSIZE % WINSIZE[0]
            stream.yPos = random.randint(0,50)
            stream.speed = random.randint(5,50)
            self.streamList.append(stream)
        pg.mixer.init()
        pg.mixer.music.load('music/matrix.mp3')
        pg.mixer.music.play()
          

    def run(self):
        
        space = 0
        while space == 0:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        space = 1
                        
        timer = time.monotonic()
        while not self.quit:
            # Timing
            timer2 = time.monotonic()
            timeDiff = timer2 - timer
            timer = timer2
            
            
            # Input
            for ev in pg.event.get():
                if ev.type == pg.KEYDOWN:
                    if ev.key == pg.K_ESCAPE:
                        self.quit = True  
            # Logic

            # Display
            self.DS.fill(BLACK)
            for stream in self.streamList:
                stream.draw(self.DS)
                stream.incYPos(stream.speed,timeDiff)
                if (stream.yPos * FONTSIZE) >= WINSIZE[1]:
                    stream.yPos = 0.0
                    stream.speed = random.randint(5,50)
            self.screen.blit(self.DS,(0,0))
            pg.display.update()
            

            

    def prepareTextStream(self,text):
        textstream = textStream(text)
        return textstream


class textStream:
    def __init__(self,text):
        self.col = 0
        self.text = text
        self.yPos = 0.0
        self.xPos = 0
        self.fontSize = FONTSIZE
        self.font = pg.font.SysFont("Arial",self.fontSize)
        
    def print(self):
        pass

    def draw(self,surf):
        for ind,char in enumerate(self.text):
            cIndex = (ind + int(self.yPos)) % len(self.text)

            if self.speed < 15.0:
                colour = DARKGREEN
            elif self.speed > 35:
                colour = LIGHTGREEN
            else:
                colour = GREEN
                
            if ind == len(self.text)-1:
                colour = WHITEGREEN
            elif ind > len(self.text)-5:
                colour = WHITISHGREEN
                
            lett = self.font.render(self.text[cIndex],True,colour)
            surf.blit(lett, (self.xPos,int((self.yPos + ind) * FONTSIZE) % WINSIZE[1]) )
        
            
            
    def incYPos(self,num,timeDiff):
        self.yPos += num * timeDiff

            

#Main
pg.init()
pg.font.init()
demo = MatrixRain("Matrix Rain")
demo.run()
pg.quit()


