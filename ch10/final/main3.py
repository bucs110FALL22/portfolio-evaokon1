import pygame
import sys
from pygame.locals import *
from random import randint

#define colors
black = (0,0,0)
white = (255,255,255)
#variables for screen size and border width
screen_height = 300
screen_width = 300
screen_size = 900
singleblock_size = screen_size // 3
line_width = 6

#variable to create grid
notfilled = float('inf')
vec2 = pygame.math.Vector2

#empty list for grid
XO = []

#initial screen
initscreen = pygame.display.set_mode((screen_height,screen_width))

#create empty 3 x 3 list to represent the grid
for x in range (3):
	row = [0] * 3
	XO.append(row)

#sets top left caption to game name
pygame.display.set_caption('Tic Tac Toe')

#main runner class and method
class Runner:
  def __init__(self, board):
    self.board = board
    self.ximg = self.imagefitting(path = 'markers/x.png', res = [singleblock_size] * 2)
    self.oimg = self.imagefitting(path = 'markers/o.png', res = [singleblock_size] * 2)
    self.grid = [[notfilled, notfilled, notfilled],
                [notfilled, notfilled, notfilled],
                [notfilled, notfilled, notfilled]]
    self.turn = randint(0,1)

  #scales image to board
  @staticmethod
  def imagefitting(path, res):
    img = pygame.image.load(path)
    return pygame.transform.smoothscale(img, res)

  #if grid space is not equal to notfilled we display X and O
  def draw_objects(self):
    for y, row in enumerate(self.grid):
      for x, obj in enumerate(row):
        if obj != notfilled:
          self.board.screen.blit(self.ximg if obj else self.oimg, vec2(x,y))

  def draw_board(self):
    bg = (255, 255, 255)
    grid = (50, 50, 50)
    self.screen.fill(bg)
    for x in range(3):
      pygame.draw.line(self.screen, grid, (0, 100 * x), (screen_width,100 * x), line_width)
      pygame.draw.line(self.screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)
    self.draw_objects()

  def run(self):
    self.draw_board()

#board class where events will be checked and game will be run
class Board:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((screen_height,screen_width))
    self.runner = Runner(self)
  def check_events(self):
    #checks if the user exited the application
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
  def play(self):
    playing = True
    #while playing used to check events
    while playing:
      self.runner.run()
      self.check_events()
      pygame.display.update()

if __name__ == '__main__':
  board = Board()
  board.play()