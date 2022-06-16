from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_MAX = 250
Y_SPACE = 10
APPEAR_PROB = 5
PROB_FACTOR = 0.9

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = MOVE_INCREMENT
        self.car_prob = APPEAR_PROB
        self.level = 1

    def random_car_appear(self):
        if random.randint(0, APPEAR_PROB) == APPEAR_PROB:
            self.random_car()

    def random_car(self):
        rand_y = random.randint(-Y_MAX, Y_MAX)
        rand_color = random.choice(COLORS)
        new_car = Car(rand_y, self.speed, rand_color)
        self.cars.append(new_car)

    def move(self, player_pos):
        for car in self.cars:
            move_result = car.move(player_pos)
            if move_result == 1:
                car.hideturtle()
                self.cars.remove(car)
            elif move_result == 2:
                return True
        return False

    def clear(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()

    def level_up(self):
        self.clear()
        self.level += 1
        self.car_prob *= PROB_FACTOR
        self.speed += MOVE_INCREMENT

