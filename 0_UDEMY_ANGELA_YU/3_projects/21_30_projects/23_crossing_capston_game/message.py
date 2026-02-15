from turtle import Turtle
import time


class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('#000')
        self.goto(0,0)
        
    def show_msg(self,msg):
        time.sleep(0.5)
        self.clear()
        self.write(f'{msg}', align='center', font=('Courier',14,'bold'))
        self.screen.ontimer(self.clear,1000)

    
        
        