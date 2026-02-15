from turtle import Turtle
import time

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color('#000')
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.goto(-280,250)
        self.write(f'Level: {self.level}', align='left', font=('Courier',14,'normal'))
    
    def level_upgrade(self):
        self.level += 1
        self.update_level()
    
    def show_msg(self,msg):
        time.sleep(0.5)
        self.clear()
        self.goto(0,0)
        self.write(f'{msg}', align='left', font=('Courier',14,'normal'))
        self.screen.ontimer(self.clear,1000)
        self.update_level()

    
        
        