from turtle import Turtle
CENTER = 'center'
ARIAL_FONT = ('Courier',18,'normal')
PATH = r"0_UDEMY_ANGELA_YU\\3_projects\\20_snake_game\\date.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(PATH) as data:
            self.high_score = int(data.read())
        self.color('#fff')
        self.penup()
        self.goto(x=0,y=265)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"Score = {self.score}, High Score= {self.high_score}", align= CENTER, font= ARIAL_FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over\nYour Score = {self.score}", align= CENTER, font= ARIAL_FONT)
        
    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open(PATH, mode='w') as file:
                file.write(f"\n{self.high_score}")
        
        """ with open(PATH) as file:
            content = file.readlines()
            print(content[-1])
            
            if content[-1] > str(self.high_score):
                self.high_score = content[-1] """
        
        self.clear()
        self.update_scoreboard()
        
  