
NUM_SHAPES=7 
PIX_WIDTH=32        # Scale - 32x32 pixels per segment of shape
PIX_HEIGHT=32
PLAY_WIDTH=14       # Width of playfield incl boundaries
PLAY_HEIGHT=19      # Height of playfield incl bottom border
PLAYFIELD=(PLAY_WIDTH*PIX_WIDTH, PLAY_HEIGHT*PIX_HEIGHT)
PLAY_OFFSET=160     # bit of space for score and other bits
WINSIZE=(PLAYFIELD[0]+PLAY_OFFSET,PLAY_OFFSET // 4 +PLAYFIELD[1])
# Colour constants
BLACK=(0,0,0)
CYAN=(0,255,255)
GREEN=(0,128,0)
BLUE=(0,0,128)
DARKRED=(128,0,0)
YELLOW=(255,255,0)
ORANGE=(255,155,0)
RED=(255,0,0)
WHITE=(255,255,255)
MAGENTA=(255,0,230)
