from turtle import Turtle
FONT = ('Arial', 24, 'normal')
player1_position = (-200, 250)
player2_position = (200, 250)
from player import Players
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(player1_position)
        self.write(f'{self.score1}', align='center', font=FONT)
        self.goto(player2_position)
        self.write(f'{self.score2}', align='center', font=FONT)

    def increase_score(self, player):
        if player == 'player1':
            self.goto(player1_position)
            self.write(f'{self.score1}', align='center', font=FONT)
            self.score1 += 1
            self.clear()
            self.update_scoreboard()
        if player == 'player2':
            self.goto(player1_position)
            self.write(f'{self.score2}', align='center', font=FONT)
            self.score2 += 1
        self.clear()
        self.update_scoreboard()
