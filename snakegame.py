import turtle
import random
field=turtle.Screen()
field.addshape("headup.gif")
field.addshape("headdown.gif")
field.addshape("headright.gif")
field.addshape("headleft.gif")
field.addshape("snakebody.gif")
field.bgpic("ground.gif")
snake=turtle.Turtle()
snake.shape("headup.gif")
snake.up()

snake.goto(0,0)
snake.setheading(90)
food=turtle.Turtle()
food.shape("circle")
food.speed(500)
food.color("red")
food.up()
food.goto(10,100)
pen=turtle.Turtle()
pen.up()
pen.goto(0,250)
pen.hideturtle()
pen.color("white")
pen.write("food score=0",font=("courier",27,"bold"))
score=0
def move():
    snake.forward(15)
def up():
    if snake.heading()!=270:
        snake.setheading(90)
        snake.shape("headup.gif")
def right():
    if snake.heading()!=180:
        snake.setheading(0)
        snake.shape("headright.gif")
def down():
    if snake.heading()!=90:
        snake.setheading(270)
        snake.shape("headdown.gif")
segment=[]       
def left():
    if snake.heading()!=0:
        snake.setheading(180)
        snake.shape("headleft.gif")
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()
while True:
    if snake.distance(food)<20:
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        food.setpos(x,y)
        score=score+1
        pen.clear()
        pen.write(("food score={}").format(score),font=("courier",27,"bold"))
        
        body=turtle.Turtle()
        body.up()
        body.speed(0)
        body.shape("snakebody.gif")
        segment.append(body)
    for i in range(len(segment)-1,0,-1):
        a=segment[i-1].xcor()
        b=segment[i-1].ycor()
        segment[i].goto(a,b)
    if len(segment)>0:
        x=snake.xcor()
        y=snake.ycor()
        segment[0].setpos(x,y)
    move()
    if snake.ycor()>290:
        snake.setpos(0,0)
        field.bgpic("gameover.gif")
        food.hideturtle()
        snake.hideturtle() 
        body.hideturtle() 
    if snake.xcor()>290:
        snake.setpos(0,0)
        field.bgpic("gameover.gif")
        snake.hideturtle()
        food.hideturtle()
        body.hideturtle()
    if snake.xcor()<-290:
        snake.setpos(0,0)
        field.bgpic("gameover.gif")
        body.hideturtle()
        snake.hideturtle()
        food.hideturtle()
    if snake.ycor()<-290:
        snake.setpos(0,0) 
        field.bgpic("gameover.gif")
        food.hideturtle() 
        body.hideturtle() 
        snake.hideturtle()
turtle.done()