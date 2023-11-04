from turtle import Turtle
import random


class Food(Turtle):
    # creating food
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.9, 0.9)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    # randomizing food after being eaten up by snake
    def refresh(self):
        xcor = random.randint(-270, 270)
        ycor = random.randint(-270, 270)
        self.goto(xcor, ycor)
