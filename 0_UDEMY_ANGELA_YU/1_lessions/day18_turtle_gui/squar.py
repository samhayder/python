from turtle import Turtle,Screen
import random

box = Turtle()

def square_box():
    for _ in range(4):
        box.forward(150)
        box.right(90)


def dash():
    for _ in range(15):
        box.forward(10)
        box.penup()
        box.forward(15)
        box.pendown()

color_lists = ["navy","dark orange","medium violet red","dark orchid","antique white"]
def draw_shape(num_shape):
    angle = 360 / num_shape
    for _ in range(num_shape):
        box.forward(100)
        box.right(angle)
for num_shape_n in range(3,11):
    box.color(random.choice(color_lists))
    draw_shape(num_shape=num_shape_n)


 




screen = Screen()
screen.exitonclick()