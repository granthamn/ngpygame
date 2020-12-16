import pygame
import sys
import random
from pytris_consts import *
from tetromino import Tetrominos
from tetromino import Tetromino

class pyTrisGame:
    
    def __init__(self, caption):
        """ Constructor - Initialise vars"""

        self.update_time_delay = 0
        self.draw_time_delay = 0
        self.game_over = False
        self.score = 0
        self.highscore = 0
        self.currSpeed = 15
        self.speedCount = 0
        self.moveDown = False
        self.pieceCount = 0
        self.lineCount = 0
        # Create a surface onto which playfield will be drawn
        self.displaySurface = pygame.display.set_mode(WINSIZE)
        pygame.display.set_caption(caption)
        # This initialises the empty playfield drawing only the borders
        self.playfield=[[0 if (x != 0 and x != 13 and y != PLAY_HEIGHT-1) else 8 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]

        # List of possible Tetrominos
        self.tetrominos = Tetrominos()
        # Random Starting piece
        self.pieceNum = random.randint(0,6)
        self.nextPieceNum = random.randint(0,6)
        #self.pieceNum = 1
        self.gameOver = False
        # Complete lines
        self.lineList = []
        self.QuitGame = False
        
    def setup(self):
        # Set up first piece
        self.currentPiece = Tetromino(self.tetrominos[self.pieceNum].shape, self.tetrominos[self.pieceNum].colour, 0, 5)
        self.nextPiece = Tetromino(self.tetrominos[self.nextPieceNum].shape, self.tetrominos[self.nextPieceNum].colour, 5, 14)
        
        self.font = pygame.font.SysFont("Arial",16,True)
        self.goFont = pygame.font.SysFont("Comic Sans MS",72,True)
        self.scoreString = "Score: " + str(self.score)
        self.hiscoreString = "Hi: " + str(self.highscore)
        self.piecesString = "Pieces: " + str(self.pieceCount)
        self.linesString = "Lines: " + str(self.lineCount)
        self.scoreText = self.font.render(self.scoreString,True,WHITE)
        self.hiscoreText = self.font.render(self.hiscoreString,True,WHITE)
        self.piecesText = self.font.render(self.piecesString,True, WHITE)
        self.linesText = self.font.render(self.linesString,True,WHITE)
        self.gameOverString = "You Died"
        self.goText = self.goFont.render(self.gameOverString,True,RED)
        self.npString = "Next Piece:"
        self.npText = self.font.render(self.npString,True,WHITE)
            
       
           
    def play(self):
        pygame.font.init()
        gameTime = pygame.time.Clock()
        while not self.QuitGame:
            
            self.timer = 0
            
            self.setup()

            # Main Game loop - x and y are opposite of what is intuitive and I can't be arsed to change it all.
            # x = y axis and y = x axis
            while not self.gameOver and not self.QuitGame:
                    
                # Timing - crude at the moment will sort later    
                pygame.time.wait(50)
                self.speedCount += 1
                self.moveDown = (self.speedCount == self.currSpeed) # Piece will drop one row every n game loops
            
                # Events / User Input
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.QuitGame = True
            
                # Game Logic - Handle key presses
                self.timer += gameTime.tick()
                if self.timer > 50:
                    self.currentPiece.update(self.playfield)
                    self.timer = 0

                # Check it's time to move the current piece down the field
                if (self.moveDown):
                    # Check piece fits where it is going to be moved to
                    if self.currentPiece.fits(self.currentPiece.xPos + 1, self.currentPiece.yPos, False, self.playfield):
                        self.currentPiece.xPos += 1   
                        self.speedCount = 0
                    else:
                        # Next piece move doesn't fit - update counters. Drop speed increases every 15 pieces
                        self.score += 10
                        self.pieceCount += 1
                        if self.pieceCount % 15 == 0:
                            if self.currSpeed >=3:
                                self.currSpeed -= 1
                            else:
                                self.currSpeed += 5 # give respite if survived to this point
             
                        # Lock the piece into the playfield so it gets rendered as part of it
                        for col in range(0,4):
                            for row in range(0,4):
                                if self.currentPiece.shape[col][row] != 0:
                                    self.playfield[self.currentPiece.xPos+col][self.currentPiece.yPos+row] = self.currentPiece.shape[col][row]
                        

                        # Check for a full line, if full line, highlight
                        for col in range(0,4):
                            self.matchLine = True
                            if self.currentPiece.xPos + col < PLAY_HEIGHT - 1:
                                for row in range(1,PLAY_WIDTH-1):
                                    if self.playfield[self.currentPiece.xPos+col][row] == 0:
                                        self.matchLine = False
                                        break # Crash out at first empty square
                                    
                                # So if we're here we have a full matching line. Make a list of matched lines
                                if self.matchLine == True:
                                    self.lineList.append(self.currentPiece.xPos+col)
                                    for row in range(1,PLAY_WIDTH-1):
                                        self.playfield[self.currentPiece.xPos+col][row] = 9 # Magenta for complete line
                                        
                        # Score increases exponentially if multiple lines matched rather than just 1
                        # Encourages risk/reward
                        self.score = self.score + (len(self.lineList) ** 2) * 100
                                
                        # Ready for next piece
                        self.speedCount = 0
                        self.pieceNum = random.randint(0,6)
                        self.currentPiece = self.nextPiece
                        self.currentPiece.xPos = 0
                        self.currentPiece.yPos = 5
                        self.nextPiece = Tetromino(self.tetrominos[self.pieceNum].shape, self.tetrominos[self.pieceNum].colour, 5, 14)
                    
                        if not self.currentPiece.fits(self.currentPiece.xPos + 1, self.currentPiece.yPos, False, self.playfield):
                            self.gameOver = True # Game over if new piece can't fit on board
                    
            
                # Render Screen
                self.drawframe()              
            
            self.dogameover()
            self.reset()            
            
        pygame.quit()
        sys.exit()

    def dogameover(self):
        self.displaySurface.blit(self.goText, (((PLAY_WIDTH // 2) * PIX_WIDTH) - 148, ((PLAY_HEIGHT // 2) * PIX_HEIGHT - 64))) 
        self.highscore = self.score if self.score > self.highscore else self.highscore
        self.score = 0
        pygame.display.update()
        pygame.time.wait(5000)
        
    def drawframe(self):
        self.displaySurface.fill(BLACK) # Wipe display
        
        self.draw() # Render playfield
        self.currentPiece.draw(self.displaySurface) # Render current piece
        self.drawGrid() # Draw gridlines
        self.nextPiece.draw(self.displaySurface) # Show next piece in sidebar
            
        self.scoreString = "Score: " + str(self.score)
        self.piecesString = "Pieces: " + str(self.pieceCount)
        self.linesString = "Lines: " + str(self.lineCount)
        self.scoreText = self.font.render(self.scoreString,True,WHITE)
        self.piecesText = self.font.render(self.piecesString,True, WHITE)
        self.linesText = self.font.render(self.linesString,True,WHITE)
        self.displaySurface.blit(self.scoreText,((PLAY_WIDTH*PIX_HEIGHT) + 20, 50))
        self.displaySurface.blit(self.hiscoreText,((PLAY_WIDTH*PIX_HEIGHT) + 20, 70))
        self.displaySurface.blit(self.piecesText, ((PLAY_WIDTH*PIX_HEIGHT) + 20, 90))
        self.displaySurface.blit(self.linesText, ((PLAY_WIDTH*PIX_HEIGHT) + 20, 110))
        self.displaySurface.blit(self.npText, ((PLAY_WIDTH*PIX_HEIGHT) + 20, 130))
        pygame.display.update() # Show frame           
        if len(self.lineList):
            pygame.time.wait(200)
            self.lineList.clear()

            
    def reset(self):
        self.displaySurface.fill(BLACK)
        self.gameOver = False
        self.playfield=[[0 if (x != 0 and x != 13 and y != PLAY_HEIGHT-1) else 8 for x in range(PLAY_WIDTH)] for y in range(PLAY_HEIGHT)]
        self.speedCount = 0
        self.moveDown = False
        self.currSpeed = 15
        self.pieceCount = 0
        self.lineCount = 0
        self.pieceNum = random.randint(0,6)
        self.nextPieceNum = random.randint(0,6)
        self.currentPiece = Tetromino(self.tetrominos[self.pieceNum].shape, self.tetrominos[self.pieceNum].colour, 0, 5)
        self.currentPiece = Tetromino(self.tetrominos[self.pieceNum].shape, self.tetrominos[self.pieceNum].colour, 5, 14)

    def drawGrid(self):
        for y in range(1,PLAY_WIDTH-1):
            pygame.draw.line(self.displaySurface,(100,100,100),(y*PIX_HEIGHT,0),(y*PIX_HEIGHT,((PLAY_HEIGHT-1)*PIX_HEIGHT)-1))
        for x in range(1,PLAY_HEIGHT-1):
            pygame.draw.line(self.displaySurface,(100,100,100),(PIX_WIDTH,x*PIX_HEIGHT),(((PLAY_WIDTH-1)*PIX_WIDTH)-1,x*PIX_HEIGHT))
                
          
    def draw(self):

        # Render the playfield            
        for x in range(PLAY_HEIGHT):
            for i in range(PLAY_WIDTH):
                if self.playfield[x][i] > 0:
                    self.charRect = pygame.Rect(i*PIX_HEIGHT,x*PIX_WIDTH,PIX_WIDTH,PIX_HEIGHT)
                    # value determines the colour
                    pygame.draw.rect(self.displaySurface,self.tetrominos[self.playfield[x][i]-1].colour,self.charRect)
          
        # Check if we have matched lines
        # if so pop all matched lines from playfield list
        if len(self.lineList):
            for line in self.lineList:
                self.playfield.pop(line)
                # insert dummy row back at top of playfield to maintain shape of it.
                self.playfield.insert(0,[8,0,0,0,0,0,0,0,0,0,0,0,0,8])
                self.lineCount += 1

                
# Main 
pygame.init()
game=pyTrisGame('Pytris')
game.play()
