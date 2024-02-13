from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(0, -300)
        self.pendown()
        self.setheading(90)
        self.width(5)

        for i in range(-300, 300, 30):
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()