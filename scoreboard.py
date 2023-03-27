from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.level += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)