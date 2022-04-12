from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.color("white")
        self.get_highscore()

    def get_score(self):
        self.write(f"Score: {self.score}  Highscore: {self.high_score}", font=("Sans", 20, "bold"), align="center")

    def get_highscore(self):
        try:
            with open("score.txt", mode="r") as data:
                self.high_score = int(data.read())
        except:
            pass
        self.get_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", font=("Sans", 20, "bold"), align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.get_score()