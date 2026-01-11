from turtle import Turtle
CENTER = 'center'
ARIAL_FONT = ('Courier',24,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('#fff')
        self.penup()
        self.goto(x=0,y=270)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align= CENTER, font= ARIAL_FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over\nYour Score = {self.score}", align= CENTER, font= ARIAL_FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()