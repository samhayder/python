from turtle import Turtle,Screen,colormode,circle
import random

tim = Turtle()
colormode(255)
tim.speed('fastest')

def rgb_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def spirograph(num_of_gap):
    for _ in range(int(360/num_of_gap)):
        tim.color(rgb_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + num_of_gap)

spirograph(8)






screen = Screen()
screen.exitonclick()