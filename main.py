from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def count_num(num):
    count_nums = Turtle()
    count_nums.ht()
    count_nums.color("white")
    count_nums.penup()
    count_nums.goto(0, 20)
    for i in range(1,num):
        count_nums.clear()
        count_nums.write(num - i, font=("Sans", 20, "bold"), align="center")
        time.sleep(1)
    count_nums.clear()

count_num(4)

start_game = True
while start_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.increase_snake()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or \
            snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        score.game_over()
        start_game = False

    for snake_body in snake.snake_body:
        if snake_body == snake.head:
            pass
        elif snake.head.distance(snake_body) < 10:
            score.game_over()
            start_game = False

screen.exitonclick()

