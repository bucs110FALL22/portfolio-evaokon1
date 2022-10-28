# Needs a main


import turtle
t = turtle.Turtle()

t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()
t.up()

def eye(color, radius):
  t.goto(40, 130)
  t.fillcolor(color)
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  t.down()

def eye2(color, radius):
  t.up()
  t.goto(-40, 130)
  t.fillcolor(color)
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  t.down()

def smile(radius, width):
  t.up()
  t.goto(-60, 90)
  t.down()
  t.right(90)
  t.circle(radius, width)

eye("black", 15)
eye2("black", 15)
smile(60, 180)