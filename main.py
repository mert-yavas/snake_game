# Import necessary modules
from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

# Set up the game screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialize game elements
snake = Snake()
food = Food()
board = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        board.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            board.game_over()

# Close the game screen on click
screen.exitonclick()
