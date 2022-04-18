import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("bouncing kkk")
wn.tracer(1)

colors = ["blue", "yellow", "green", "cyan", "red", "pink", "white"]
balls = []
shapes = ["circle"]


for _ in range(1):
    balls.append(turtle.Turtle())


for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.speed(0)
    ball.penup()
    x = random.randint(-200, 290)
    y = random.randint(50, 300)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(2, 7)
    ball.da = random.randint(-5, 5)

gravity = 1

while True:
    wn.update()
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        if ball.xcor() > 195:
            ball.dx *= -1
            ball.da *= -1

        if ball.xcor() < -195:
          
            ball.dx *= -1
            ball.da *= -1

        if ball.ycor() < -270:
            ball.sety(-270)
            ball.dy *= -1
            ball.da *= -1




print(balls)







wn.mainloop()