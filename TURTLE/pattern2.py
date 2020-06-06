import turtle

turtle.speed(0)
turtle.color('black')
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.hideturtle()
side = 20

for i in range(1, 100):
    turtle.forward(side)
    turtle.left(92)
    side += 7

turtle.done()
