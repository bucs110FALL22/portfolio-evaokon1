import pygame
pygame.init()
XO = []
screen_height = 300
screen_width = 300
line_width = 6
screen = pygame.display.set_mode((screen_width, screen_height))
black = (0, 0, 0)

clicked = False
player = 1
pos = (0,0)
XO = []
game_over = False
winner = 0

class X():
  def __init__(self, xpos, ypos):
    self.xpos = xpos
    self.ypos = ypos

#create empty 3 x 3 list to represent the grid
for x in range (3):
	row = [0] * 3
	XO.append(row)

def draw_board():
	bg = (255, 255, 255)
	grid = (50, 50, 50)
	screen.fill(bg)
	for x in range(1,3):
		pygame.draw.line(screen, grid, (0, 100 * x), (screen_width,100 * x), line_width)
		pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)

def draw_markers():
	x_pos = 0
	for x in XO:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, black, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
				pygame.draw.line(screen, black, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
			if y == -1:
				pygame.draw.circle(screen, black, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
			y_pos += 1
		x_pos += 1

def check_game_over():
	global game_over
	global winner

	x_pos = 0
	for x in XO:
		#check vertical wins
		if sum(x) == 3:
			winner = 1
			game_over = True
		if sum(x) == -3:
			winner = 2
			game_over = True
		#check horizontal wins
		if XO[0][x_pos] + XO[1][x_pos] + XO[2][x_pos] == 3:
			winner = 1
			game_over = True
		if XO[0][x_pos] + XO[1][x_pos] + XO[2][x_pos] == -3:
			winner = 2
			game_over = True
		x_pos += 1

	#check diagonal wins
	if XO[0][0] + XO[1][1] + XO[2][2] == 3 or XO[2][0] + XO[1][1] + XO[0][2] == 3:
		winner = 1
		game_over = True
	if XO[0][0] + XO[1][1] + XO[2][2] == -3 or XO[2][0] + XO[1][1] + XO[0][2] == -3:
		winner = 2
		game_over = True

	#check for tie
	if game_over == False:
		tie = True
		for row in XO:
			for i in row:
				if i == 0:
					tie = False
		#if it is a tie, then call game over and set winner to 0
		if tie == True:
			game_over = True
			winner = 0