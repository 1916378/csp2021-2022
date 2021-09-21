import turtle as trtl
#describe turtle as painter to help better understand the code 
painter = trtl.Turtle()
wn = trtl.Screen()
wn.bgcolor("#87CEFA")
painter.speed(100)

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
painter.goto(-200,-110)
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

#create base house
painter.penup()
painter.pencolor("black")
painter.fillcolor("#EBEAE1")
painter.begin_fill()
painter.goto(-50,-50)
painter.pendown()
wall = 0
while (wall < 2):
  painter.forward(100)
  painter.left(90)
  painter.forward(80)
  painter.left(90)
  wall = wall + 1
painter.end_fill()

#congress
painter.begin_fill()
painter.left(180)
painter.forward(120)
painter.right(90)
painter.forward(65)
painter.right(90)
painter.forward(120)
painter.right(90)
painter.forward(65)
painter.end_fill()

#other side of congress
painter.penup()
painter.left(90)
painter.goto(50,-50)
painter.pendown()
painter.begin_fill()
painter.forward(120)
painter.left(90)
painter.forward(65)
painter.left(90)
painter.forward(120)
painter.left(90)
painter.forward(65)
painter.end_fill()

#roof
painter.penup()
painter.goto(-50,30)
painter.left(90)

painter.begin_fill()
painter.pendown()
painter.left(20)
painter.goto(0,50)
painter.right(90)
painter.goto(50,30)
painter.right(110)
painter.forward(100)
painter.end_fill()

painter.begin_fill()
painter.right(90)
painter.forward(10)
painter.right(90)
painter.forward(23)
painter.goto(-50,30)
painter.end_fill()

painter.penup()
painter.goto(50,30)
painter.pendown()
painter.begin_fill()
painter.left(90)
painter.forward(10)
painter.left(90)
painter.forward(23)
painter.goto(50,30)
painter.end_fill()

#windows 
painter.penup()
painter.right(180)
painter.goto(-160,-15)
painter.fillcolor("#8593c0")
painter.pendown()

windowtopleft = 0
while (windowtopleft < 4):
  painter.begin_fill()
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.end_fill()
  painter.penup()
  painter.forward(30)
  painter.pendown()
  windowtopleft = windowtopleft + 1

painter.penup()
painter.goto(-160,-45)
painter.pendown()

windowbottomleft = 0
while (windowbottomleft < 4):
  painter.begin_fill()
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.end_fill()
  painter.penup()
  painter.forward(30)
  painter.pendown()
  windowbottomleft = windowbottomleft + 1

painter.penup()
painter.goto(160,-45)
painter.right(180)
painter.pendown()

windowbottomright = 0
while (windowbottomright < 4):
  painter.begin_fill()
  painter.forward(10)
  painter.right(90)
  painter.forward(20)
  painter.right(90)
  painter.forward(10)
  painter.right(90)
  painter.forward(20)
  painter.right(90)
  painter.end_fill()
  painter.penup()
  painter.forward(30)
  painter.pendown()
  windowbottomright = windowbottomright + 1

painter.penup()
painter.goto(160,5)
painter.pendown()

windowtopright = 0
while (windowtopright < 4):
  painter.begin_fill()
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.end_fill()
  painter.penup()
  painter.forward(30)
  painter.pendown()
  windowtopright = windowtopright + 1

painter.penup()
painter.right(90)
painter.forward(5)
painter.left(90)
painter.forward(6)
painter.pendown()

topwindow = 0
while (topwindow < 3):
  painter.begin_fill()
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.end_fill()
  painter.penup()
  painter.forward(30)
  painter.pendown()
  topwindow = topwindow + 1

painter.penup()
painter.right(180)
painter.forward(20)
painter.right(90)
painter.forward(55)
painter.left(90)
painter.pendown()

bottomwindow = 0
while (bottomwindow < 2):
  painter.begin_fill()
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.forward(10)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.end_fill()
  painter.penup()
  painter.forward(60)
  painter.pendown()
  bottomwindow = bottomwindow + 1
  

#pillars
painter.penup()
painter.goto(-45,-50)
painter.pencolor("black")
painter.fillcolor("#dcceb9")
painter.pendown()

painter.begin_fill()
painter.forward(10)
painter.left(90)
painter.forward(80)
painter.left(90)
painter.forward(10)
painter.left(90)
painter.forward(80)
painter.left(90)
painter.end_fill()

painter.penup()
painter.goto(35,-50)
painter.pendown()
painter.begin_fill()
painter.forward(10)
painter.left(90)
painter.forward(80)
painter.left(90)
painter.forward(10)
painter.left(90)
painter.forward(80)
painter.left(90)
painter.end_fill()

painter.penup()
painter.goto(-25,-50)
painter.pendown()
painter.begin_fill()
painter.forward(10)
painter.left(90)
painter.forward(80)
painter.left(90)
painter.forward(10)
painter.left(90)
painter.forward(80)
painter.left(90)
painter.end_fill()

painter.penup()
painter.goto(15,-50)
painter.pendown()
painter.begin_fill()
painter.forward(10)
painter.left(90)
painter.forward(80)
painter.left(90)
painter.forward(10)
painter.left(90)
painter.forward(80)
painter.end_fill()

#door
painter.penup()
painter.goto(-10,-50)
painter.fillcolor("brown")
painter.begin_fill()
painter.pendown()
painter.left(90)
painter.forward(20)
painter.left(90)
painter.forward(30)
painter.left(90)
painter.forward(20)
painter.left(90)
painter.forward(30)
painter.end_fill()

#flag
painter.penup()
painter.goto(0,0)
painter.left(180)
painter.forward(50)

painter.pencolor("grey")
painter.pensize(2)
painter.pendown()

painter.forward(40)
painter.right(90)
painter.pencolor("black")
painter.fillcolor("red")
painter.penup()
painter.begin_fill()

painter.forward(30)
painter.right(90)
painter.forward(15)
painter.right(90)
painter.forward(30)
painter.right(90)
painter.forward(15)
painter.end_fill()

#stripes
painter.penup()
painter.fillcolor("white")
painter.right(180)
painter.forward(2)
painter.left(90)
painter.pencolor("white")
painter.pensize(2)
painter.pendown()

painter.forward(30)
painter.penup()
painter.right(90)
painter.forward(4)
painter.right(90)
painter.pendown()
painter.forward(30)

painter.left(90)
painter.penup()
painter.forward(4)
painter.left(90)
painter.pendown()
painter.forward(30)

#blue
painter.penup()
painter.left(90)
painter.goto(0,0)
painter.forward(90)
painter.right(90)
painter.fillcolor("blue")

painter.begin_fill()
painter.forward(10)
painter.right(90)
painter.forward(10)
painter.right(90)
painter.forward(10)
painter.right(90)
painter.end_fill()

#bushes
painter.penup()
painter.right(90)
painter.pencolor("green")
painter.fillcolor("green")
painter.goto(-160,-50)
painter.turtlesize(1.5)
painter.shape("circle")

bushes = 0
while (bushes < 16):
  painter.stamp()
  painter.forward(20)
  bushes = bushes + 1

# Save Screen
wn = trtl.Screen()
wn.mainloop()