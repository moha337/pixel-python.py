import turtle

ground=turtle.Turtle()
ground=turtle.Screen()
ground.bgpic('field.png')
ground.addshape("blueman.gif") #right
ground.addshape("yellowman.gif") #left
ground.addshape("ball.gif")
right=turtle.Turtle()
right.up()
right.shape("blueman.gif")
right.goto(400,100)
left=turtle.Turtle()
left.up()
left.shape("yellowman.gif")
left.goto(-400,-100)
ball=turtle.Turtle()
ball.up()
ball.shape("ball.gif")
def leftmanfor():
    x=left.xcor()
    left.setx(x+50)
    
def leftback():
    x=left.xcor()
    left.setx(x-50)
leftscore=0
rscore=0
   
def leftr():
    y=left.ycor()
    left.sety(y+50)
def leftl():
    y=left.ycor()
    left.sety(y-50)
def rightfor():
    x=right.xcor()
    right.setx(x+50)   
def rightb():
    x=right.xcor()
    right.setx(x-50)
def rightr():
    y=right.ycor()
    right.sety(y+50)
def rightl():
    y=right.ycor()
    right.sety(y-50)
win=turtle.Turtle()
win.penup()
win.hideturtle()
win.color("Gold")

leftpen=turtle.Turtle()
leftpen.penup()
leftpen.hideturtle()
leftpen.goto(-450,250)
leftpen.color("white")
leftpen.write("leftplayer score: 0",font=("courier",27,"bold"))
rpen=turtle.Turtle()
rpen.penup()
rpen.hideturtle()
rpen.goto(50,250)
rpen.color("white")
rpen.write("Rightplayer score: 0",font=("courier",27,"bold"))
turtle.listen()
turtle.onkeypress(leftmanfor,"d")
turtle.onkeypress(leftback,"a")
turtle.onkeypress(leftr,"w")
turtle.onkeypress(leftl,"s")
turtle.onkeypress(rightb,"Left")
turtle.onkeypress(rightfor,"Right")
turtle.onkeypress(rightr,"Up")
turtle.onkeypress(rightl,"Down")
dx=5
dy=-5
while True:
    x=ball.xcor()
    y=ball.ycor()
    ball.setpos(x+dx,y+dy)
    if right.distance(ball)<50:
        dx=-dx
    if left.distance(ball)<50:
        dx=-dx
    if ball.ycor()> 280:
        dy=-dy
    if ball.ycor()<-280:
        dy=-dy
    if ball.xcor()<-450:
        ball.goto(0,0)
        rpen.clear()
        rscore=rscore+1
        rpen.write(("Rightplayer score: {}").format(rscore),font=("courier",27,"bold"))

    if ball.xcor()>450:
       ball.goto(0,0)
       leftpen.clear()
       leftscore=leftscore+1
       leftpen.write(("leftplayer score: {}").format(leftscore),font=("courier",27,"bold"))
    if leftscore>=15:
         win.goto(-100,0)
         win.write(("Win👑"),font=("courier",27,"bold"))
    if rscore>=15:
        win.goto(100,0)
        win.write(("Win👑"),font=("courier",27,"bold"))
turtle.listen()
turtle.done()
