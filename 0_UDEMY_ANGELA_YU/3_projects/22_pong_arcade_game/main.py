from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
  

screen = Screen()
screen.setup(width=1200,height=800)
screen.bgcolor('#000')
screen.title('Pong Game')
screen.tracer(0)


left_paddle = Paddle((-580,0))
right_paddle = Paddle((570,0))
ball = Ball()
scoreboard = Scoreboard()

# ss = Turtle()
# ss.color('white')
# ss.goto(-70,200)
# ss.write('00', align='center', font=("Courier",88,"normal"))

screen.listen()
screen.onkey(left_paddle.go_up,'4')
screen.onkey(left_paddle.go_down,'1')
screen.onkey(right_paddle.go_up,'6')
screen.onkey(right_paddle.go_down,'3')

game_is_on = False

while not game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()
    
    # Detect collision with wall & bounce
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(right_paddle) < 25 and ball.xcor() > 380 or ball.distance(left_paddle) < 25 and ball.xcor() < -380:
        ball.bounce_x()
    
    # Detect when Left paddle misses
    if ball.xcor() < -600:
        ball.reset_position()
        scoreboard.right_point()
        
    # Detect when Right paddle misses
    if ball.xcor() > 600:
        ball.reset_position()
        scoreboard.left_point()
    

screen.exitonclick()