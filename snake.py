from turtle import Turtle
import random
position=[(0,0),(-20,0),(-40,0)]
STEPS=20
UP,DOWN,LEFT,RIGHT = 90,270,180,0
COLORS=['violet','indigo','blue','green','yellow','red']
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for pos in position:
            self.add_segment(pos)
    def add_segment(self,pos):
            new_block=Turtle()
            new_block.shape('square')
            new_block.color(random.choice(COLORS))
            new_block.penup()
            new_block.goto(pos)
            self.segments.append(new_block)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def  move(self):
        for seg in range(len(self.segments)-1,0,-1):
            x=self.segments[seg-1].xcor()
            y=self.segments[seg-1].ycor()
            self.segments[seg].goto(x,y)
        self.segments[0].forward(STEPS)

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
    def reset(self):
        for seg in  self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]



