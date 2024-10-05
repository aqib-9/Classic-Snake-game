from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open('data.txt') as data:
         score=int(data.read())
         self.highscore=score
        self.color('white')
        self.penup()
        self.goto(0,210)
        self.clear_screen()
        self.hideturtle()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', 'w') as data:
                data.write(f'{self.highscore}')
        self.score=0
        self.clear_screen()

    def clear_screen(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore}",align='center',font=('Aerial', 24, 'normal'))
       
    def increase(self):
        self.score+=1
        self.clear()
        self.clear_screen()