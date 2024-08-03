from turtle import Turtle, Screen
from player1 import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(-400,0)
paddle_2 = Paddle(400,0)
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 370 or ball.ycor() < -370:
        ball.bounce()
    
    if paddle_2.distance(ball) < 30 and ball.xcor() > 320 or paddle_1.distance(ball) < 30 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 470:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_score()
    
    
    if ball.xcor() < -470:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_score()   
        

screen.exitonclick()