import turtle
radius =200
turtle.getscreen().colormode(255)
turtle.speed(0)
turtle.setposition(0, 0)
for i in range(1,50):
    r,g,b=255,150,110
    turtle.pencolor((r,g,b))
    turtle.circle(radius,360,50)
    radius-=10



turtle.done()

