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
pong_ball.dx = (100)
pong_ball.dy = (100)
pong_ball.penup()
pong_ball.goto(0, 0)

sc.mainloop()