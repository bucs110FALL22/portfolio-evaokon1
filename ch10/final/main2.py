#import modules
import pygame
from pygame.locals import *
from X import X
# from O import O
from X import draw_markers
from X import check_game_over
from X import draw_board

pygame.init()

screen_height = 300
screen_width = 300
line_width = 6
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')

#define colors
black = (0, 0, 0)
white = (255, 255, 255)

#define font
font = pygame.font.SysFont(None, 40)

#define variables
clicked = False
player = 1
pos = (0,0)
XO = []
game_over = False
winner = 0

#main loop
run = True
while run:

	#draw board and markers first
	draw_board()
	draw_markers()

	#handle events
	for event in pygame.event.get():
		#handle game exit
		if event.type == pygame.QUIT:
			run = False
		#run new game
		if game_over == False:
			#check for mouseclick
			if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
				clicked = True
			if event.type == pygame.MOUSEBUTTONUP and clicked == True:
				clicked = False
				pos = pygame.mouse.get_pos()
				cell_x = pos[0] // 100
				cell_y = pos[1] // 100
				if XO[cell_x][cell_y] == 0:
					XO[cell_x][cell_y] = player
					player *= -1
					check_game_over()

	#check if game has been won
	if game_over == True:
		draw_game_over(winner)

	#update display
	pygame.display.update()

pygame.quit()