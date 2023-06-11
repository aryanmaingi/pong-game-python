import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.tracer(0)
paddle_l = Paddle((350, 0))
paddle_r = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(paddle_l.goup, "Up")
screen.onkey(paddle_l.down, "Down")
screen.onkey(paddle_r.goup, "w")
screen.onkey(paddle_r.down, "s")




game = True
while game:
    ball.move()
    time.sleep(ball.ball_speed)
    screen.update()

    #detect collision on right
    if ball.xcor() > 380:
        time.sleep(1)
        ball.reset_y()
        score.sc_l += 1
        score.refresh()

    # detect collision on left
    if ball.xcor() < -380:
        time.sleep(1)
        ball.reset_x()
        score.sc_r += 1
        score.refresh()

    #detect collision with paddle
    if paddle_l.distance(ball) < 50 and ball.xcor() > 320 or paddle_r.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()



    #detect collision on top and down
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()



screen.exitonclick()