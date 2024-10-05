from turtle import Turtle,Screen
import time
from snake  import Snake
from  food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(500,500)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
game_on=True

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if snake.head.xcor() >  240 or snake.head.xcor() < -250 or snake.head.ycor() > 240 or  snake.head.ycor() < -240:
        scoreboard.reset()
        snake.reset()
    
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()
        






class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top != -1:
            value = self.stack[self.top]
            self.top -= 1
            return value
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.top + 1)):
            self.stack[i] += val







screen.exitonclick()