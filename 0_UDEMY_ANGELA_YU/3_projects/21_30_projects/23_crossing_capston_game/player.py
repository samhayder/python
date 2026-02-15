from turtle import Turtle

START_POSITION = (0,-280)
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.goto(START_POSITION)
        self.setheading(UP)
    
    
    def turn_up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)
    
    def turn_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)
    
    def turn_left(self):
        self.setheading(LEFT)
        self.forward(MOVE_DISTANCE)
        
    def turn_right(self):
        self.setheading(RIGHT)
        self.forward(MOVE_DISTANCE)
        
    def reset_player(self):
        self.goto(START_POSITION)