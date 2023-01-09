import turtle

sc = turtle.Screen()
sc.title("Tech Project")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=2)
# stretch causes small bounce zone, find way to draw rectangle
paddle_a.penup()
paddle_a.goto(-400, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=2)
paddle_b.penup()
paddle_b.goto(400, 0)

pong_ball = turtle.Turtle()
pong_ball.speed(10)
pong_ball.shape("circle")
pong_ball.color("red")
pong_ball.movevectorx = 5
pong_ball.movevectory = -5
pong_ball.penup()
pong_ball.goto(0, 0)
#pong_ball.shapesize(stretch_wid=3, stretch_len=3), unnecessary
#ball possibly too fast, change later, DONE

player_one = 0
player_two = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("player_one : 0    player_two : 0",
            align="center", font=("arial", 24, "normal"))

#started creating the paddles here
#Paddle positioning
def paddleaup():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddleadown():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddlebup():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddlebdown():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

#QUESTION this is where I add in key functions, but they do not work, FIXED
sc.listen()
sc.onkeypress(paddleadown, "a")
sc.onkeypress(paddleaup, "z")
sc.onkeypress(paddlebdown, "Up")
sc.onkeypress(paddlebup, "Down")

running = True
while running == True:
    #set variable running = True above loop, change loop to while running == True, DONE
    sc.update()

    pong_ball.setx(pong_ball.xcor()+pong_ball.movevectorx)
    pong_ball.sety(pong_ball.ycor()+pong_ball.movevectory)
    #change all movevectorx and movevectory to movevectorx and movevectory, DONE

    if pong_ball.ycor() > 280:
            pong_ball.sety(280)
            pong_ball.movevectory *= -1

    if pong_ball.ycor() < -280:
            pong_ball.sety(-280)
            pong_ball.movevectory *= -1
            #sety (280), movevectory *= -1, done

    if pong_ball.xcor() > 500:
            pong_ball.goto(0, 0)
            pong_ball.movevectory *= -1 #won't need once ball is randomized
            player_one += 1
            sketch.clear()
            sketch.write("player_one : {} player_two: {}".format(
                        player_one, player_two), align="center",
                        font=("arial", 24, "normal"))

    if pong_ball.xcor() < -500:
            pong_ball.goto(0, 0)
            pong_ball.movevectory *= -1
            player_two += 1
            sketch.clear()
            sketch.write("player_one : {} player_two: {}".format(
                                    player_one, player_two), align="center",
                                    font=("arial", 24, "normal"))
#set restart direction to randomize between 4 options, do after break, call every time I want to randomize start

    if (pong_ball.xcor() > 360 and pong_ball.xcor() < 370) and (pong_ball.ycor() < paddle_b.ycor()+40 and pong_ball.ycor() > paddle_b.ycor()-40):
            pong_ball.setx(360)
            pong_ball.movevectorx*=-1

    if (pong_ball.xcor()<-360 and pong_ball.xcor()> -370) and (pong_ball.ycor()<paddle_a.ycor()+40 and pong_ball.ycor()>paddle_a.ycor()-40):
            pong_ball.setx(-360)
            pong_ball.movevectorx*=-1
#paddle is a box, test for where ball bounces from paddle based on stretch, maybe stretching in odd direction

#sc.mainloop() unnecessary