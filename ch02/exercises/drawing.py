import turtle
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length: "))
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")
screen = turtle.Screen()
angle = 360.0/sides
for i in range(sides):
  t.forward(length)
  t.left(angle)
screen.exitonclick()