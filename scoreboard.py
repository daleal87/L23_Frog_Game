from turtle import Turtle
FONT = ("Courier", 20, "normal")
SCORE_POS = (-280, 260)
TEXT_ALIGN = "left"
GAMEOVER_ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POS)
        self.level = 1
        self.update()

    def level_up(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align=TEXT_ALIGN, font=FONT)

    def game_over(self):
        self.update()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=GAMEOVER_ALIGN, font=FONT)
