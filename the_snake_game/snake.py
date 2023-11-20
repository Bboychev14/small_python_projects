from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_cor = 0
        for _ in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x_cor, 0)
            x_cor -= 20
            self.segments.append(new_segment)

    def add_segment(self):
        x_cor = self.segments[-1].xcor()
        y_cor = self.segments[-1].ycor()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        if self.head.heading() == 90:
            y_cor -= 20
            new_segment.goto(x_cor, y_cor)
            self.segments.append(new_segment)
        elif self.head.heading() == 180:
            x_cor += 20
            new_segment.goto(x_cor, y_cor)
            self.segments.append(new_segment)
        elif self.head.heading() == 270:
            y_cor += 20
            new_segment.goto(x_cor, y_cor)
            self.segments.append(new_segment)
        elif self.head.heading() == 0:
            x_cor -= 20
            new_segment.goto(x_cor, y_cor)
            self.segments.append(new_segment)

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            x_coordinates = self.segments[segment_index - 1].xcor()
            y_coordinates = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(x_coordinates, y_coordinates)
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