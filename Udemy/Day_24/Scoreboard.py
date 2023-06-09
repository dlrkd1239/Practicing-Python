from turtle import Turtle

font = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("snake_highscore.txt") as file:
            self.highscore = int(file.read())
        self.user_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.user_score}, Highscore : {self.highscore}", False, "center", font)

    def over(self):
        if self.user_score > self.highscore:
            self.highscore = self.user_score
            with open("snake_highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.user_score = 0
        self.write_score()

        # self.write("Game Over", False, "center", font)

    def increase(self):
        self.clear()
        self.user_score += 1
        self.write_score()
