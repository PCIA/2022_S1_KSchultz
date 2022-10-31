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
paddle_a.goto(-400, 0)
