from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sc_r = 0
        self.sc_l = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(f"{self.sc_l} ", align="center", font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(f"{self.sc_r} ", align="center", font=('Courier', 80, 'normal'))

    def refresh(self):
        self.clear()
        self.update()
