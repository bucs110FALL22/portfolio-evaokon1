import turtle
import random

inScreen = True
t = turtle.Turtle()

window = turtle.Screen()
window.bgcolor('lightblue')

while inScreen:
  r = random.randint(1,2)
  if r == 1:
    t.left(90)
  else:
    t.right(90)
  t.forward(10)

  txcor = t.xcor()
  tycor = t.ycor()
  xrange = window.window_width()/2
  yrange = window.window_height()/2

  if abs(txcor) > xrange or abs(tycor) > yrange:
    inScreen = False

window.exitonclick()