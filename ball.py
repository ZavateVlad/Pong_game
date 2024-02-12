from turtle import Turtle
import random
from player import Players

direction_list = [170]
random_direction = random.choice(direction_list)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.setheading(random_direction)
        #random_x = random.choice(range(-290, 290))
        #random_y = random.choice(range(-290, 290))
        #self.ball.goto(random_x, random_y)

    def move_ball(self):
        #direction_list = [0, 90, 180, 270]
        #self.setheading(random_direction)
        self.forward(10)

    def bounce(self):
        last_heading = self.heading()
        self.setheading(last_heading + 180)
        #self.forward(20)

