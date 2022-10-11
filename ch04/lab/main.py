import pygame
import turtle
pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#window = turtle.Screen()
#window.bgcolor('blue')
color = pygame.color.Color('#C00A21')

screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width, screen_height])

t = turtle.Turtle()

r = screen_width
pygame.draw.circle(screen, 'red', (0,0), 3)
