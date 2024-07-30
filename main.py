from turtle import Turtle, Screen
from player1 import Paddle

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(-400,0)
paddle_2 = Paddle(400,0)

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")



game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()