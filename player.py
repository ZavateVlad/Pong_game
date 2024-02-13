from turtle import Turtle


class Players(Turtle):
    def __init__(self):
        super().__init__()

    def create_player(self, position):
            self.shape('square')
            self.color('white')
            self.shapesize(stretch_wid=1, stretch_len=5)
            self.penup()
            self.speed('fastest')
            self.goto(position)
            self.setheading(90)

    def up(self):
        self.setheading(90)

    def down(self):
        self.setheading(270)

    def change_direction(self):
        if self.ycor() < -290:
            self.up()

        elif self.ycor() > 290:
            self.down()