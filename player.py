from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SHAPE = "turtle"
COLOR = "black"
SAVING_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.go_to_start()

    def go_to_start(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def is_saved(self):
        if self.ycor() > SAVING_Y:
            self.go_to_start()
            return True
        return False


