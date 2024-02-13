# Breakdown of the project
# 1 Show 2 players, the ball, the dotted line X
# 2 Move the players X
# 3 Move the ball X
# 4 Set playing field - ball needs to bounce at the those field limits
# 5 Set scoreboard
# 6 Decide winning game - first to 12
# 7 Decide losing point - not hitting the ball - the ball resets

# Classes
# Class for players - 4 blocks of white, which are moving on the y axis
# Class for ball - 1 block of white, which is bouncing when touching the player, resets if it ends on X = 300 (not hitting the player)
# Class for scoreboard - show score, everytime the ball resets, add a point to the other player, might inherit from the ball class
# Class for field - set boundaries, might inherit from the ball class


from turtle import Screen
from player import Players
from ball import Ball
from field import Field
from scoreboard import Scoreboard

screen = Screen()
screen.setworldcoordinates(-300, -300, 300, 300)
screen.bgcolor('black')
player1_pos = (-280, -40)
player2_pos = (280, -40)
scoreboard = Scoreboard()
ball = Ball()
field = Field()
player1 = Players()
player2 = Players()
player1.create_player(player1_pos)
player2.create_player(player2_pos)

screen.listen()
screen.onkeypress(player1.up, 'Up')
screen.onkeypress(player1.down, 'Down')
screen.onkeypress(player2.up, 'w')
screen.onkeypress(player2.down, 's')

is_playing = True

while is_playing:
    player1.forward(10)
    player2.forward(10)
    ball.move_ball()

    # Detect collision with player
    if player1.distance(ball) < 20 or player2.distance(ball) < 20:
        ball.bounce_off_players()
        ball.move_ball()

    # Change direction for both players if the field limit is reached
    if player1.ycor() > 290 or player1.ycor() < -290:
        player1.change_direction()

    if player2.ycor() > 290 or player2.ycor() < -290:
        player2.change_direction()

    # Detect collision with edges
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_off_limits()
        ball.move_ball()

    # Condition for score point
    if ball.xcor() > 290:
        scoreboard.increase_score('Player1')
        ball.reset()

    if ball.xcor() < -290:
        scoreboard.increase_score('Player2')
        ball.reset()

    #Condition to win
    if scoreboard.score1 == 12 or scoreboard.score2 == 12:
        scoreboard.game_over()
        is_playing = False
screen.exitonclick()
