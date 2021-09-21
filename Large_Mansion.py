#   This code draws a mansion.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

#Screen
wn = trtl.Screen()
trtl.bgcolor("sky blue")

#house
painter.penup()
painter.goto(-170, -150)
painter.pendown()
painter.pensize(5)
painter.pencolor("#EAE3C9")
painter.fillcolor("#EAE3C9")
painter.begin_fill()
painter.goto(-170, 75)
painter.goto(160,75)
painter.goto(160,-150)
painter.goto(-170, -150)
painter.end_fill()

#roof
painter.penup()
painter.goto(-200,60)
painter.pensize(7)
painter.pencolor("brown")
painter.pendown()
painter.fillcolor("burlywood")
painter.begin_fill()
painter.goto(-5,150)
painter.goto(200,60)
painter.penup()
painter.goto(160,75)
painter.pendown()
painter.goto(-165,75)
painter.end_fill()

#door
painter.penup()
painter.fillcolor("burlywood")
painter.begin_fill()
painter.goto(60,-150)
painter.pendown()
painter.left(90)
painter.forward(70)
painter.circle(65,180)
painter.forward(70)
painter.left(90)
painter.forward(130)
painter.end_fill()
painter.penup()
painter.goto(-5,-18)
painter.pendown()
painter.right(90)
painter.forward(132)
painter.penup()
painter.goto(-27,-74)
painter.shape("circle")
painter.color("brown")
painter.turtlesize(0.5)
painter.stamp()
painter.goto(16,-74)
painter.stamp()

# windows
painter.goto(-52,43)
painter.pendown()
sides = 0
painter.fillcolor("light sky blue")
painter.begin_fill()
while sides < 4:
  painter.forward(30)
  painter.right(90)
  sides = sides + 1
painter.end_fill()
painter.penup()
painter.goto(67,43)
painter.pendown()
painter.begin_fill()
sides = 0
while sides < 4:
  painter.forward(30)
  painter.right(90)
  sides = sides + 1
painter.end_fill()

# stem left
painter.color("green")
painter.pensize(5)
painter.penup()
painter.goto(-145, -150)
painter.setheading(90)
painter.pendown()
painter.forward(100)
painter.backward(30)

# leaf left
painter.setheading(270)
painter.circle(10, 120, 20)
painter.setheading(90)
painter.goto(-145, -70)

# rest of stem left
painter.forward(30)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(0.5)

# draw flower left
painter.color("darkorchid")
painter.goto(-140,20)
petals = 0
while (petals < 18):
  painter.right(20)
  painter.forward(10)
  painter.stamp()
  petals = petals + 1
  
# ring 2 of flower left
painter.goto(-140,10)
painter.color("blue")
petals = 0
while (petals < 12):
  painter.right(30)
  painter.forward(10)
  painter.stamp()
  petals = petals + 1

#ring 3 of flower left
painter.goto(-140,0)
painter.color("yellow")
petals = 0
while (petals < 6):
  painter.right(60)
  painter.forward(10)
  painter.stamp()
  petals = petals + 1

# stem right
painter.color("green")
painter.pensize(5)
painter.penup()
painter.goto(135, -150)
painter.setheading(90)
painter.pendown()
painter.forward(100)
painter.backward(30)

# leaf right
painter.setheading(270)
painter.circle(10, 120, 20)
painter.setheading(90)
painter.goto(135, -70)

# rest of stem right
painter.forward(30)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(0.5)

# draw flower right
painter.color("darkorchid")
painter.goto(140,20)
petals = 0
while (petals < 18):
  painter.right(20)
  painter.forward(10)
  painter.stamp()
  petals = petals + 1
  
# ring 2 of flower right
painter.goto(140,10)
painter.color("blue")
petals = 0
while (petals < 12):
  painter.right(30)
  painter.forward(10)
  painter.stamp()
  petals = petals + 1

#ring 3 of flower right
painter.goto(140,0)
painter.color("yellow")
petals = 0
while (petals < 6):
  painter.right(60)
  painter.forward(10)
  painter.stamp()
  petals = petals + 1


'''
#Coordinates for debug
tess=trtl.Turtle() 
 
# self defined function to print coordinate
def buttonclick(x,y):
    print("You clicked at this coordinate({0},{1})".format(x,y))
 
 #onscreen function to send coordinate
trtl.onscreenclick(buttonclick,1)
trtl.listen()  # listen to incoming connections
trtl.speed(10) # set the speed
'''

# hide turtle
painter.penup()
painter.goto(500,500)

# hold the screen
wn.mainloop()