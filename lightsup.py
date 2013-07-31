#!/usr/bin/env python2.7
# Light's Up

import random, pygame, sys
from pygame.locals import *

# Constants
FPS = 30 # frames per second
WINDOWWIDTH = 640 # pixels
WINDOWHEIGHT = 480 # pixels
BOXSIZE = 40 # size of box - height/width, in pixels
GAPSIZE = 10 # size of gap between boxes, in pixels
BOARDWIDTH = 10 # no of cols of icons
BOARDHEIGHT = 7 # no of rows of icons

assert(BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxses for pairs of matches.'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) /2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) /2)

# Colours     R   G   B 
GREY      = (100,100,100)
STEELBLUE  = (64,134,170)

WHITE     = (255,255,255)
RED       = (255,0,0)
GREEN     = (0,255,0)
BLUE      = (0,0,255)
YELLOW    = (255,255,0)
ORANGE    = (255,128,0)
PURPLE    = (255,0,255)
CYAN      = (0,255,255)

BGCOLOUR = STEELBLUE
LIGHTBGCOLOUR = GREY
BOXCOLOUR = WHITE
HIGHLIGHTCOLOUR = BLUE

ALLCOLOURS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)

def main():
  global FPSCLOCK, DISPLAYSURF
  pygame.init()
  FPSCLOCK = pygame.time.Clock()
  DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

  mousex = 0
  mousey = 0
  pygame.display.set_caption('Lights Up!')

  firstSelection = None # stores the (x,y) of the first box clicked.

  DISPLAYSURF.fill(BGCOLOUR)

  mainBoard = getStartBoard()
  drawBoard(mainBoard)
  # Redraw the screen and wait a clock tick.
  pygame.display.update()
  FPSCLOCK.tick(FPS)
  
  while True:
    mouseClicked = False

    DISPLAYSURF.fill(BGCOLOUR)
    drawBoard(mainBoard)

    for event in pygame.event.get():
      if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
        pygame.quit()
        sys.exit()
      elif event.type == MOUSEMOTION:
        mousex, mousey = event.pos
      elif event.type == MOUSEBUTTONUP:
        mousex, mousey = event.pos
        mouseClicked = True

    boxx, boxy = getBoxAtPixel(mousex, mousey)
    if boxx != None and boxy != None:
      # The mouse is currently over a box.
      drawHighlightBox(boxx, boxy)
      if mouseClicked:
        continue

      # Redraw the screen and wait a clock tick.
      pygame.display.update()
      FPSCLOCK.tick(FPS)

def getStartBoard():
  # Create the board data structure, with randomly placed icons.
  board = []
  for x in range(BOARDWIDTH):
    column = []
    board.append(column)
  return board
  
def splitIntoGroupsOf(groupSize, theList):
  # splits a list into a list of lists, where the inner lists have at 
  # most groupSize of items.
  result = []
  for i in range(0, len(theList), groupSize):
    result.append(theList[i:i + groupSize])
  return result

def leftTopCoordsOfBox(boxx, boxy):
  # Convert board coordinates to pixel coordinates
  left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
  top  = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
  return (left, top)

def getBoxAtPixel(x, y):
  for boxx in range(BOARDWIDTH):
    for boxy in range(BOARDHEIGHT):
      left, top = leftTopCoordsOfBox(boxx, boxy)
      boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
      if boxRect.collidepoint(x, y):
        return (boxx, boxy)
  return (None, None)

def drawBoard(board):
  for boxx in range(BOARDWIDTH):
    for boxy in range(BOARDHEIGHT):
      left, top = leftTopCoordsOfBox(boxx, boxy)
      pygame.draw.rect(DISPLAYSURF, BOXCOLOUR, (left, top, BOXSIZE, BOXSIZE))

def drawHighlightBox(boxx, boxy):
  left,top = leftTopCoordsOfBox(boxx, boxy)
  pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOUR, (left - 5, top -5, BOXSIZE + 10, BOXSIZE + 10), 4)

def gameWonAnimation(board):
  pass

def hasWon(revealedBoxes):
  pass

if __name__ == '__main__':
  main()

