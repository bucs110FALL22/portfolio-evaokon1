import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
for i in range(10):
  num = random.randint(0,10)
  num2 = random.randint(0,10)

for i in range(10):
  michelangelo.forward(num)
  leonardo.forward(num2)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()

coords = []
num_sides = 3
side_length = 120
offset = 100

for i in range(3):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append(x)
  coords.append(y)
  
pygame.draw.polygon(coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(lightblue)

num_sides = 4
side_length = 90
offset = 100

for i in range(4):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append(x)
  coords.append(y)
  
pygame.draw.polygon(coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(lightblue)

num_sides = 6
side_length = 60
offset = 100

for i in range(6):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append(x)
  coords.append(y)
  
pygame.draw.polygon(coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(lightblue)

num_sides = 9
side_length = 40
offset = 100

for i in range(9):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append(x)
  coords.append(y)
  
pygame.draw.polygon(coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(lightblue)

num_sides = 360
side_length = 1
offset = 100

for i in range(360):
  theta = (2.0 * math.pi * i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append(x)
  coords.append(y)
  
pygame.draw.polygon(coords)
pygame.display.flip()
pygame.time.wait(1000)
window.fill(lightblue)

window.exitonclick()