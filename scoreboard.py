from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Arial", 30, "normal")


class Score:
    def __init__(self):
        self.turtle = Turtle()
        self.score = 0
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.color("black")
        self.turtle.goto(x=0, y=250)
        self.score_update()

    def score_update(self):
        self.turtle.clear()
        self.turtle.write(f"SCORE: {self.score}/50", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.score_update()

