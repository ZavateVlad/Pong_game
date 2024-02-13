from turtle import Turtle
import random

STARTING_POSITION = [20, 160, 200, 340]
PLAYER_BOUNCE = random.choice(range(-30, 30))


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.reset()

    def move_ball(self):
        self.forward(10)

    def bounce_off_players(self):
        last_heading = self.heading()
        self.setheading(last_heading + 180 + PLAYER_BOUNCE)

    def bounce_off_limits(self):
        last_heading = self.heading()
        self.setheading(last_heading + 90)

    def reset(self):
        self.goto(0, 0)
        random_direction = random.choice(STARTING_POSITION)
        self.setheading(random_direction)

