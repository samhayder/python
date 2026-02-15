from turtle import Turtle,Screen
import random

is_user_bet = False
colors = ["red","green","blue","pink","purple","navy"]
y_position = [-70,-40,-10,20,50,80]
turtle_lists = []

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Witch turtle will win the race? Enter a color: ")

if user_bet:
    is_user_bet = True

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.setpos(x=-230,y=y_position[turtle_index])
    turtle_lists.append(tim)


while is_user_bet:
    for turtle in turtle_lists:
        if turtle.xcor() > 230:
            is_user_bet = False
            wining_color = turtle.pencolor()
            
            if user_bet == wining_color:
                print(f"You've Win. The wining color is- {wining_color}")
            else:
                print(f"You've Lose. The wining color is- {wining_color}")
                
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        

screen.exitonclick()