from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_body = []
        for i in STARTING_POSITIONS:
            self.add_body(i)
        self.head = self.snake_body[0]

    def add_body(self, position):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.snake_body.append(new_body)

    def increase_snake(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
            for seg_num in range(len(self.snake_body)-1, 0, -1):
                new_x = self.snake_body[seg_num - 1].xcor()
                new_y = self.snake_body[seg_num - 1].ycor()
                self.snake_body[seg_num].goto(new_x, new_y)
            self.head.forward(20)



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
