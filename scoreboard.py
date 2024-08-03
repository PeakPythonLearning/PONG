from turtle import Turtle

TEXT = ("Courier", 80, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_score()
       

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align= "center", font=TEXT)
        self.goto(100, 200)
        self.write(self.rscore, align= "center", font=TEXT)

    def l_point(self):
        self.lscore += 1
    
    def r_point(self):
        self.rscore += 1

