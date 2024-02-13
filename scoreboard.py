from turtle import Turtle
FONT = ('Arial', 24, 'normal')
player1_score = (-200, 250)
player2_score = (200, 250)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(player1_score)
        self.write(f'{self.score}', align='center', font=FONT)
        self.goto(player2_score)
        self.write(f'{self.score}', align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()