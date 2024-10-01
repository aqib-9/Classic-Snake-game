from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(0,210)
        self.clear_screen()
        self.hideturtle()

    def clear_screen(self):
        self.write(f"Score : {self.score}",align='center',font=('Aerial', 24, 'normal'))
       
    def increase(self):
        self.score+=1
        self.clear()
        self.clear_screen()
    def  game_over(self):
        self.goto(0,0)
        self.write(f"Game Over! Final Score : {self.score}",align='center',font=('Aerial', 24, 'normal'))
        
