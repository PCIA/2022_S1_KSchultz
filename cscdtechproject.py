import turtle

sc = turtle.Screen()
sc.title("Tech Project")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=10, stretch_len=6)
paddle_a.penup()
paddle_a.goto(-600, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=10, stretch_len=6)
paddle_b.penup()
paddle_b.goto(600, 0)

pong_ball = turtle.Turtle()
pong_ball.speed(40)
pong_ball.shape("circle")
pong_ball.color("red")
pong_ball.dx = 5
pong_ball.dy = -5
pong_ball.penup()
pong_ball.goto(0, 0)
pong_ball.shapesize(stretch_wid=3, stretch_len=3)

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

def paddleaup():
    y = paddle_a.ycor
    y += 20
    paddle_a.sety(y)

def paddleadown():
    y = paddle_a.ycor
    y -= 20
    paddle_a.sety(y)

def paddlebup():
    y = paddle_b.ycor
    y += 20
    paddle_b.sety(y)

def paddlebdown():
    y = paddle_b.ycor
    y -= 20
    paddle_b.sety(y)

sc.listen()
sc.onkeypress(paddleaup, "a")
sc.onkeypress(paddleadown, "z")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

while True:
    sc.update

    pong_ball.setx()

sc.mainloop()