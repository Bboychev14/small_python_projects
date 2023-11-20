from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.clear()
        self.write(f"Game Over!", align="center", font=("Courier", 24, "normal"))
        self.goto(0, 0)
        self.write(f"Your final score is: {self.score}", align="center", font=("Courier", 24, "normal"))