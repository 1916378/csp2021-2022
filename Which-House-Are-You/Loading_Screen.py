import turtle as trtl
painter = trtl.Turtle()

print("Loading...")

#Spinning turtle
painter.shape("turtle")
painter.pencolor("black")
painter.fillcolor("green")

load = 0
while (load < 15):
  painter.right(100)
  load = load + 1
painter.hideturtle()