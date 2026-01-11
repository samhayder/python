from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snakes()
        self.head = self.segments[0]
    
    # Create Snake
    def create_snakes(self):
        for position in STARTING_POSITION:
            self.add_snake(position)
    
    def add_snake(self,position):
        snake_shape = Turtle(shape='square')
        snake_shape.color('#fff')
        snake_shape.penup()
        snake_shape.goto(position)
        self.segments.append(snake_shape)
        
    def extend_snake(self):
        self.add_snake(self.segments[-1].position())
    
    # Move the snake     
    def move(self):
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    # Controlling snake by keypress
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)