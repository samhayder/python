from turtle import Turtle
import random

CARS_COLORS = ['green','blue','yellow','pink','orange','purple']
MOVE_DISTANCE = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        
    def create_car(self):
        random_change = random.randint(1,6)
        if random_change == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(stretch_wid=0.5,stretch_len=1.5)
            new_car.color(random.choice(CARS_COLORS))
            new_car.penup()
            new_ycor = random.randint(-250,250)
            new_car.goto(x=300,y=new_ycor)
            self.all_cars.append(new_car)
    
    def car_move(self):
        for i in self.all_cars:
            i.back(MOVE_DISTANCE)
    
    

            
        