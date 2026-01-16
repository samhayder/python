import time
from turtle import Screen
from player import Player
from level import Level
from message import Message
from car_manager import CarManager


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('#ddd')
screen.tracer(0)

player = Player()
level = Level()
message = Message()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.turn_up,key="Up")
screen.onkey(fun=player.turn_down,key="Down")
screen.onkey(fun=player.turn_left,key="Left")
screen.onkey(fun=player.turn_right,key="Right")

game_is_on = False

while not game_is_on:
    screen.update()
    time.sleep(0.1)
    
    car_manager.create_car()
    car_manager.car_move()
        
    # Detect collision in cars
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            message.show_msg('GAME OVER')
            game_is_on = True
        elif player.ycor() > 280:
            level.level_upgrade()
            player.reset_player()
            message.show_msg("Level upgrade")
        elif player.xcor() > 280 or player.xcor() < -280:
            player.turn_up()
            player.reset_player()
            message.show_msg("Wrong way!")
    
        
screen.exitonclick()