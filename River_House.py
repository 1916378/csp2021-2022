import turtle as trtl
#describe turtle as painter to help better understand the code 
painter = trtl.Turtle()
wn = trtl.Screen()
painter.speed(100)
wn.bgcolor("#87CEFA")

#create the scenery 
painter.penup()
painter.goto(-200,-50)
painter.pencolor("#5AAB61")
painter.pendown()
painter.fillcolor("#5AAB61")
painter.begin_fill()
#loop to make ground
ground = 0
while (ground < 4): 
  painter.forward(400)
  painter.right(90)
  ground = ground + 1
painter.end_fill()
#another ground shade 
painter.penup()
painter.goto(-200,-60)
painter.pencolor("#358856")
painter.pendown()
painter.fillcolor("#358856")
painter.begin_fill()
#loop to make ground
ground = 0
while (ground < 4): 
  painter.forward(400)
  painter.right(90)
  ground = ground + 1
painter.end_fill()
#river
painter.penup()
painter.goto(-200,-90)
painter.pencolor("#007577")
painter.pendown()
painter.fillcolor("#007577")
painter.begin_fill()
#loop to make river
ground = 0
while (ground < 4): 
  painter.forward(400)
  painter.right(90)
  ground = ground + 1
painter.end_fill()

#create tree trunk 1
painter.penup()
painter.goto(-150,-50)
painter.pencolor("brown")
painter.fillcolor("brown")
painter.begin_fill()
painter.pendown()
painter.forward(10)
painter.left(90)
painter.forward(50)
painter.left(90)
painter.forward(10)
painter.left(90)
painter.forward(50)
painter.end_fill()


#create leaves 1
painter.penup()
painter.fillcolor("#013220")
painter.pencolor("#013220")
painter.right(180)
painter.forward(50)
painter.right(90)
painter.forward(5)
painter.left(90)
painter.shapesize(2)
painter.pendown()
painter.shape("triangle")
painter.stamp()
painter.forward(20)
painter.stamp()
painter.shape("classic")

#create tree trunk 2
painter.penup()
painter.goto(150,-50)
painter.pencolor("brown")
painter.fillcolor("brown")
painter.begin_fill()
painter.right(90)
painter.pendown()
painter.forward(10)
painter.left(90)
painter.forward(50)
painter.left(90)
painter.forward(10)
painter.left(90)
painter.forward(50)
painter.end_fill()

#create leaves 2
painter.penup()
painter.fillcolor("#013220")
painter.pencolor("#013220")
painter.right(180)
painter.forward(50)
painter.right(90)
painter.forward(5)
painter.left(90)
painter.shapesize(2)
painter.pendown()
painter.shape("triangle")
painter.stamp()
painter.forward(20)
painter.stamp()
painter.shape("classic")

#create tree trunk 3
painter.penup()
painter.goto(100,-50)
painter.pencolor("brown")
painter.fillcolor("brown")
painter.begin_fill()
painter.right(90)
painter.pendown()
painter.forward(10)
painter.left(90)
painter.forward(40)
painter.left(90)
painter.forward(10)
painter.left(90)
painter.forward(40)
painter.end_fill()

#create leaves 3
painter.penup()
painter.fillcolor("#013220")
painter.pencolor("#013220")
painter.right(180)
painter.forward(40)
painter.right(90)
painter.forward(5)
painter.left(90)
painter.shapesize(2)
painter.pendown()
painter.shape("triangle")
painter.stamp()
painter.forward(20)
painter.stamp()
painter.shape("classic")

#create tree trunk 4
painter.penup()
painter.goto(-100,-50)
painter.pencolor("brown")
painter.fillcolor("brown")
painter.begin_fill()
painter.right(90)
painter.pendown()
painter.forward(10)
painter.left(90)
painter.forward(40)
painter.left(90)
painter.forward(10)
painter.left(90)
painter.forward(40)
painter.end_fill()

#create leaves 4
painter.penup()
painter.fillcolor("#013220")
painter.pencolor("#013220")
painter.right(180)
painter.forward(40)
painter.right(90)
painter.forward(5)
painter.left(90)
painter.shapesize(2)
painter.pendown()
painter.shape("triangle")
painter.stamp()
painter.forward(20)
painter.stamp()
painter.shape("classic")


#create house
painter.penup()
painter.right(90)
painter.goto(-40,-50)
painter.pencolor("#EAE3C9")
painter.fillcolor("#EAE3C9")
painter.begin_fill()
painter.pendown()
walls = 0
while (walls < 4):
  painter.forward(80)
  painter.left(90)
  walls = walls + 1
painter.end_fill()

#create roof
painter.penup()
painter.left(90)
painter.forward(80)
painter.right(45)
painter.pencolor("red")
painter.fillcolor("red")
painter.begin_fill()
painter.pendown()
painter.forward(57)
painter.right(90)
painter.forward(57)
painter.right(135)
painter.forward(80)
painter.end_fill()

#create window outline 
painter.penup()
painter.pencolor("brown")
painter.fillcolor("brown")
painter.goto(-20,0)
painter.shape("square")
painter.shapesize(1.1)
painter.stamp()
painter.penup()
painter.goto(20,0)
painter.pendown()
painter.stamp()

#create windows 
painter.penup()
painter.pencolor("#ADD8E6")
painter.fillcolor("#ADD8E6")
painter.goto(-20,0)
painter.shape("square")
painter.shapesize(1)
painter.stamp()
painter.penup()
painter.goto(20,0)
painter.pendown()
painter.stamp()

#create door 
painter.shape("classic")
painter.penup()
painter.goto(-10,-50)
painter.right(180)
painter.pencolor("brown")
painter.fillcolor("brown")
painter.begin_fill()
painter.pendown()
door = 0
while (door < 2):
  painter.forward(20)
  painter.left(90)
  painter.forward(30)
  painter.left(90)
  door = door + 1
painter.end_fill()

#doorknob
painter.penup()
painter.pencolor("yellow")
painter.fillcolor("yellow")
painter.shape("circle")
painter.turtlesize(.25)
painter.goto(4,-38)
painter.stamp()

#create sun 
painter.penup()
painter.turtlesize(5)
painter.goto(145,130)
painter.pendown()
painter.stamp()

#create clouds
painter.penup()
painter.pencolor("white")
painter.fillcolor("white")
painter.turtlesize(3)
painter.goto(-145,130)
painter.pendown()
painter.stamp()
painter.penup()
painter.goto(-125,110)
painter.pendown()
painter.stamp()
painter.penup()
painter.goto(-110,120)
painter.pendown()
painter.stamp()
painter.penup()
painter.goto(-100,110)
painter.pendown()
painter.stamp()
painter.penup()
painter.goto(-95,120)
painter.pendown()
painter.stamp()
painter.penup()
painter.goto(-75,125)
painter.pendown()
painter.stamp()

tr = trtl.Turtle()
tr.speed(100)
tr.penup()
tr.shape("turtle")
tr.goto(-200,-120)
tr.pencolor("black")
tr.fillcolor("green")


while True:
  tr.forward(.1)
  if (tr.xcor() > 210):
    tr.right(180)
  if (tr.xcor() < -210):
    tr.right(180)

# Hold Screen
wn = trtl.Screen()
wn.mainloop()