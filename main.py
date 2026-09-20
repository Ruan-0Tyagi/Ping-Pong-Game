from turtle import Screen,Turtle 
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import time



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height = 600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()
        
    #Detect collision with  paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()
        
    #Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        ball.x_move = -10
        scoreboard.l_point()
        
    #Detect when right paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        ball.x_move = 10
        scoreboard.r_point()
        
    #who win
    if scoreboard.win():
        game_is_on = False

        

screen.exitonclick()

