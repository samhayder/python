import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.pensize(15)
tim.speed("fast")

directions = [0,90,180,270]
color_list = ['royal blue','dark blue','dodger blue','deep sky blue','teal','maroon','medium violet red','dark slate blue']

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color



for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))







screen = Screen()
screen.exitonclick()