import pygame
from pytris_consts import *
import copy


class Tetromino:
    def __init__(self,tetroList, colour, xPos=0, yPos=0):
        """Constructor"""
        self.shape = tetroList
        self.colour = colour
        self.xPos = xPos        # top left coordinate of shape in playfield.
        self.yPos = yPos
        self.holdRotate = False # is user holding down rotate key?
        
    def draw(self, surface):
        """Render individual piece"""
        for colNum, col in enumerate(self.shape):
            for rowNum, row in enumerate(col):
                if row >= 1:
                    self.tetRect=pygame.Rect(self.yPos*PIX_HEIGHT+rowNum*PIX_HEIGHT,self.xPos*PIX_WIDTH+colNum*PIX_WIDTH,PIX_WIDTH,PIX_HEIGHT)
                    pygame.draw.rect(surface,self.colour,self.tetRect)
                    
                    
    def update(self,playfield):
        """ Handle user input"""
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_RIGHT] and self.fits(self.xPos,self.yPos+1,False,playfield):
            self.yPos += 1
        if keysPressed[pygame.K_LEFT] and self.fits(self.xPos,self.yPos-1,False,playfield):
            self.yPos -= 1
        if keysPressed[pygame.K_DOWN] and self.fits(self.xPos+1,self.yPos,False,playfield):
            self.xPos += 1
        if keysPressed[pygame.K_SPACE]:
            if self.holdRotate == False and self.fits(self.xPos,self.yPos,True,playfield):
                self.Rotate()
                self.holdRotate = True     # Toggle so piece doesn't rotate wildly
        else:
            self.holdRotate = False

    def fits(self,newY, newX, rotFlag,playfield):
        """Check next move of piece is valid"""
        
        for colNum, col in enumerate(self.shape):
            for rowNum, row in enumerate(col):
                if rotFlag == False:
                    rowPointer = rowNum
                    colPointer = colNum
                else:
                    rowPointer = 3 - colNum  #Handle 90 degree rot
                    colPointer = rowNum
                if row != 0 and playfield[newY+colPointer][newX+rowPointer] != 0:
                # doesn't fit, do one
                    return False
        return True
                
    def Rotate(self):
        """90 degree rotation of shape. Bit crude. Rework?"""
        newShape = copy.deepcopy(self.shape) # Create new copy of shape
        
        for colNum, col in enumerate(self.shape):       
            for rowNum, row in enumerate(col):
                newShape[rowNum][3 - colNum] = row
        self.shape = newShape
        del newShape
      
        
class Tetrominos:
    def __init__(self):
        """List of possible shapes"""
        self.tetrominos = []
        self.tetrominos.append(Tetromino([[0,1,0,0],
                                          [0,1,0,0],
                                          [0,1,0,0],
                                          [0,1,0,0]],CYAN))
        self.tetrominos.append(Tetromino([[0,0,2,0],
                                          [0,2,2,0],
                                          [0,2,0,0],
                                          [0,0,0,0]],BLUE))
        self.tetrominos.append(Tetromino([[0,3,0,0],
                                          [0,3,3,0],
                                          [0,0,3,0],
                                          [0,0,0,0]],GREEN))
        self.tetrominos.append(Tetromino([[0,0,0,0],
                                          [0,4,4,0],
                                          [0,4,4,0],
                                          [0,0,0,0]],DARKRED))
        self.tetrominos.append(Tetromino([[0,0,5,0],
                                          [0,5,5,0],
                                          [0,0,5,0],
                                          [0,0,0,0]],YELLOW))
        self.tetrominos.append(Tetromino([[0,0,6,0],
                                          [0,0,6,0],
                                          [0,6,6,0],
                                          [0,0,0,0]],ORANGE))
        self.tetrominos.append(Tetromino([[0,7,0,0],
                                          [0,7,0,0],
                                          [0,7,7,0],
                                          [0,0,0,0]],RED))
        # Dummy for border
        self.tetrominos.append(Tetromino([[0,0,0,0],
                                          [0,0,0,0],
                                          [0,0,0,0],
                                          [0,0,0,0]],WHITE))
        # Dummy for completed row
        self.tetrominos.append(Tetromino([[0,0,0,0],
                                          [0,0,0,0],
                                          [0,0,0,0],
                                          [0,0,0,0]],MAGENTA))
    def __iter__(self):
        """Need this to be able to iterate over shapes"""
        return self.tetrominos.__iter__()
    def __getitem__(self,key):
        return self.tetrominos[key]
