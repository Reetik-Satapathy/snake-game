from turtle import Turtle


class score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("highscore.txt", "r") as highscore:
            self.highsc = int(highscore.read())
        self.color("white")
        self.write(f"score={self.score} high score={self.highsc}", False, "center", ('Arial', 15, 'normal'))

    # keeping and displaying score
    def scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"score={self.score} high score={self.highsc}", False, "center", ('Arial', 15, 'normal'))

    # keeping track of high score
    def reset(self):
        if self.score > self.highsc:
            with open("highscore.txt", "w") as newhighscore:
                newhighscore.write(f"{self.score}")
                self.highsc=self.score
        self.score = 0
        self.scoreboard()
