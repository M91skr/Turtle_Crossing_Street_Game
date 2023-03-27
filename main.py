"""---------------------------------------- Turtle in the Street Game ----------------------------------------
In this code, a simple game is created. Using the keyboard(UP button), the player guides a turtle to cross the street.
As the stages of the game increase, the speed of the game also increases.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

play = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(play.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.cars_create()
    car.move_cars()

    for cars in car.all_cars:
        if play.distance(cars) < 20:
            game_is_on = False
            score.game_over()

    if play.is_at_finish_line():
        score.update_score()
        play.go_to_start()
        car.level_up()

screen.exitonclick()