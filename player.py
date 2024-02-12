from turtle import Turtle


class Players:
    def __init__(self):
        self.segments = []
        #self.head = self.segments[0]

    def create_player(self, starting_position):
        for position in starting_position:
            self.player = Turtle('square')
            self.player.color('white')
            self.player.penup()
            self.player.speed('fastest')
            self.player.goto(position)
            self.segments.append(self.player)
            self.head = self.segments[0]
            self.segments[-1].setheading(90)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.x_coord = self.segments[seg_num - 1].xcor()
            self.new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(self.x_coord, self.new_y)
        self.head.forward(10)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)



