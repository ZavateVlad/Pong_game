#Breakdown of the project
#1 Show 2 players, the ball, the dotted line X
#2 Move the players X
#3 Move the ball X
#4 Set playing field - ball needs to bounce at the those field limits
#5 Set scoreboard
#6 Decide winning game - first to 12
#7 Decide losing point - not hitting the ball - the ball resets

#Classes
#Class for players - 4 blocks of white, which are moving on the y axis
#Class for ball - 1 block of white, which is bouncing when touching the player, resets if it ends on X = 300 (not hitting the player)
#Class for scoreboard - show score, everytime the ball resets, add a point to the other player, might inherit from the ball class
#Class for field - set boundaries, might inherit from the ball class


from turtle import Screen
from player import Players
from ball import Ball
from field import Field
from scoreboard import Scoreboard
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor('black')
player1_pos = [(-295, -40), (-295, -20), (-295, 0), (-295, 20), (-295, 40)]
player2_pos = [(295, -40), (295, -20), (295, 0), (295, 20), (295, 40)]
scoreboard = Scoreboard()
ball = Ball()
field = Field()
player1 = Players()
player2 = Players()
player1.create_player(player1_pos)
player2.create_player(player2_pos)





screen.listen()
screen.onkey(player1.up, 'Up')
screen.onkey(player1.down, 'Down')
screen.onkey(player2.up, 'w')
screen.onkey(player2.down, 's')

is_playing = True

while is_playing:
    player1.move()
    player2.move()
    ball.move_ball()
    for segment1, segment2 in zip(player1.segments, player2.segments):
        if segment1.distance(ball.position()) < 20 or segment2.distance(ball.position()) < 20:
            ball.bounce()
            ball.move_ball()
    print(ball.heading())

screen.exitonclick()