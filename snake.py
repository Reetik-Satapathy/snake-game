from turtle import Turtle

LOCATIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    # creating the snake body
    def create_snake(self):
        for i in LOCATIONS:
            self.create_body(i)

    def create_body(self, position):
        t = Turtle("square")
        t.speed("fastest")
        t.penup()
        t.color("white")
        t.goto(position)
        self.turtles.append(t)

    # extending snake's body
    def extend_body(self):
        self.create_body(self.turtles[-1].position())

    # moving the snake's body in various directions
    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            xcor = self.turtles[i - 1].xcor()
            ycor = self.turtles[i - 1].ycor()
            self.turtles[i].goto(xcor, ycor)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def reset(self):
        for tur in self.turtles:
            tur.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]
