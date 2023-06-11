from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create(position)

    def create(self, position):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def goup(self):
        n_y1 = self.ycor() + 20
        self.goto(self.xcor(), n_y1)

    def down(self):
        n_y2 = self.ycor() - 20
        self.goto(self.xcor(), n_y2)
