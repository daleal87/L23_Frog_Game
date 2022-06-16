import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

# Events
screen.onkey(fun=player.move, key="Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.random_car_appear()
    if car_manager.move(player.pos()):
        print("Turtle is dead :)")
        scoreboard.game_over()
        break

    if player.is_saved():
        car_manager.level_up()
        scoreboard.level_up()
    screen.update()

screen.exitonclick()
