from turtle import Turtle
from snake import Snake
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.color('blue')
        self.penup()
        self.speed('fastest')
        self.refresh()
    def refresh(self):
        xcor=random.randint(-200,200)
        ycor=random.randint(-200,200)
        self.goto(xcor,ycor)


    