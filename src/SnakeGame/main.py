import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

"""
The screen listen create a new listen object that interrupt the while loop inside the game
"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    # Screen refreshing
    time.sleep(0.1)
    # Start the snake move straight
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    x_coordinate = int(snake.head.xcor())
    y_coordinate = int(snake.head.ycor())
    print(x_coordinate, y_coordinate)

    # Detect collision with wall
    if x_coordinate > 280 or x_coordinate < -280 \
            or y_coordinate > 280 or y_coordinate < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
