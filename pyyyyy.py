import time
import snake
from turtle import Screen
from food import Food
from score import score

# setting up screen
screen = Screen()
screen.setup(600, 600)
screen.title("snake game")
screen.bgcolor("green")
screen.tracer(0)

# creating objects
snake = snake.Snake()
food = Food()
score = score()

screen.listen()

# controlling snake's movements
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

flag = True
while flag:
    # keep moving forward
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_body()
        score.scoreboard()

    # detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # detecting collision with snake's body
    for body in snake.turtles:
        if body == snake.head:
            pass
        elif snake.head.distance(body) < 15:

            score.reset()
            snake.reset()

screen.exitonclick()
