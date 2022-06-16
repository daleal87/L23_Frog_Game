from turtle import Turtle
SHAPE = "square"
SHAPE_SCALE_X = 2
SHAPE_SCALE_Y = 1
START_X = 300
GONE_X = -300
INIT_SIZE = 20


class Car(Turtle):
    def __init__(self, starting_y, speed, color):
        super().__init__()
        self.shape(SHAPE)
        self.color(color)
        self.penup()
        self.speed = speed
        self.x_size = INIT_SIZE * SHAPE_SCALE_X
        self.y_size = INIT_SIZE * SHAPE_SCALE_Y
        self.shapesize(SHAPE_SCALE_Y, SHAPE_SCALE_X)
        self.appear(starting_y)

    def appear(self, starting_y):
        self.setheading(0)
        self.goto((START_X, starting_y))

    def move(self, player_pos):
        self.setx(self.xcor() - self.speed)
        if self.has_run_over(player_pos):
            return 2
        elif self.has_gone():
            return 1
        return 0

    def has_gone(self):
        if self.xcor() < GONE_X:
            return True
        return False

    def has_run_over(self, player_pos):
        front_x = int(self.xcor() - self.x_size/2)
        back_x = int(self.xcor() + self.x_size/2)
        left_y = int(self.ycor() - self.y_size/2)
        right_y = int(self.ycor() + self.y_size/2)

        if left_y <= player_pos[1] <= right_y:
            if front_x <= player_pos[0] <= back_x:
                return True
        return False
