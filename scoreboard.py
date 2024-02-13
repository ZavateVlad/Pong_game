from turtle import Turtle
FONT_FOR_SCORE = ('Arial', 24, 'normal')
FONT_FOR_WINNER = ('Arial', 40, 'normal')
PLAYER1_SCORE_POSITION = (-200, 250)
PLAYER2_SCORE_POSITION = (200, 250)


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
        self.goto(PLAYER1_SCORE_POSITION)
        self.write(f'{self.score1}', align='center', font=FONT_FOR_SCORE)
        self.goto(PLAYER2_SCORE_POSITION)
        self.write(f'{self.score2}', align='center', font=FONT_FOR_SCORE)

    def increase_score(self, player):
        self.player = player
        if self.player == 'Player 1':
            self.goto(PLAYER1_SCORE_POSITION)
            self.write(f'{self.score1}', align='center', font=FONT_FOR_SCORE)
            self.score1 += 1
            self.clear()
            self.update_scoreboard()
        if self.player == 'Player 2':
            self.goto(PLAYER2_SCORE_POSITION)
            self.write(f'{self.score2}', align='center', font=FONT_FOR_SCORE)
            self.score2 += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 10)
        self.write(f'{self.player} wins!', align = 'center', font=FONT_FOR_WINNER)
