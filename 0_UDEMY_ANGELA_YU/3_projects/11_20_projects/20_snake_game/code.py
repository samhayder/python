from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#000")
screen.title("Snake Game in Turtle")
screen.tracer(0)

# 1. Create Snake 3 dots
staring_positions = [(0,0), (-20,0), (-40,0)]
snakes = []

for position in staring_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("#fff")
    new_segment.penup()
    new_segment.goto(position)
    snakes.append(new_segment)


is_game_start = False


    



















screen.exitonclick()