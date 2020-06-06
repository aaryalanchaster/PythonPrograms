
from turtle import Turtle, Screen

MIN_COLOR = 5
MAX_COLOR = 255

COUNT = 150
ANGLE = 5

STARTING_LENGTH = 
LENGTH_INCREMENT = 2

N = 6

def draw_polygon(turtle, size):
    angle = 360 / N
    for _ in range(N):
        turtle.forward(size)
        turtle.left(angle)


screen = Screen()
screen.colormode(255)

mega = Turtle()
mega.speed(0)

length = STARTING_LENGTH

for r in range(COUNT):
    red = round(r * ((MAX_COLOR - MIN_COLOR) / (COUNT - 1))) + MIN_COLOR
    color = (0, 0, red)

    mega.fillcolor(color)
    mega.begin_fill()
    draw_polygon(mega, length)
    mega.end_fill()

    length += LENGTH_INCREMENT
    mega.left(ANGLE)

mega.hideturtle()
screen.exitonclick()