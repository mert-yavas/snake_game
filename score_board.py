from turtle import Turtle
from snake import Snake
from food import Food


# Constants for scoreboard display
SCOREBOARD_POSITION_X = 0
SCOREBOARD_POSITION_Y = 270
ALIGNMENT = "center"
FONT = ("arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION_X, SCOREBOARD_POSITION_Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        # Display the current score
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # Display "GAME OVER" when the game ends
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # Increase the score and update the scoreboard display
        self.score += 1
        self.clear()
        self.update_scoreboard()
