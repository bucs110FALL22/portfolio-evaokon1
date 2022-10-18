import turtle
t = turtle.Turtle()
window = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.color("green")
num_sides = int(input("How many sides? "))
side_length = int(input("What is the length of one side? "))

def draw_eq_shape(t, num_sides, side_length):
  angle = 360/num_sides
  for i in range(num_sides):
    t.forward(side_length)
    t.right(angle)
draw_eq_shape(turtle, num_sides, side_length)
window.exitonclick()