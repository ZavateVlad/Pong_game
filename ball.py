from turtle import Turtle
import random

starting_direction = [20, 160, 200, 340]
player_bounce = random.choice(range(-30, 30))


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.reset()
        #random_x = random.choice(range(-290, 290))
        #random_y = random.choice(range(-290, 290))
        #self.ball.goto(random_x, random_y)

    def move_ball(self):
        #direction_list = [0, 90, 180, 270]
        #self.setheading(random_direction)
        self.forward(15)

    def bounce_off_players(self):
        last_heading = self.heading()
        self.setheading(last_heading + 180 + player_bounce)
        #self.forward(20)

    def bounce_off_limits(self):
        last_heading = self.heading()
        self.setheading(last_heading + 90)

    def reset(self):
        self.goto(0,0)
        random_direction = random.choice(starting_direction)
        self.setheading(random_direction)

