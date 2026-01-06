from turtle import Turtle,Screen
""" 
w = Forwards
s = Backwards
a = Counter-Clockwise
d = Clockwise
c = Close """


tim = Turtle()
screen = Screen()

def forwards():
    tim.fd(10)

def backwards():
    tim.back(10)

def turn_up():
    heading_position = tim.heading() + 10
    tim.setheading(heading_position)

def turn_down():
    heading_position = tim.heading() - 10
    tim.setheading(heading_position)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()

screen.onkey(key="Right", fun=forwards)
screen.onkey(key="Left", fun=backwards)
screen.onkey(key="Up", fun=turn_up)
screen.onkey(key="Down", fun=turn_down)
screen.onkey(key="Delete", fun=clear)

screen.exitonclick()

