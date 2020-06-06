import turtle
turtle.color('red')
turtle.speed(0)
side=400
turtle.penup()
turtle.goto(-300,-200)
turtle.pendown()

for i in range(1,100):
    turtle.fd(side)
    turtle.left(90)
    side-=4
turtle.done()
