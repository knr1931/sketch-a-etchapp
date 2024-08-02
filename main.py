from sketching import Turtle, SketchPen
from turtle import Screen


screen = Screen()
screen.listen()

screen.onkey(key="w", fun=SketchPen.move_forwards)
screen.onkey(key="s", fun=SketchPen.move_backwards)
screen.onkey(key="a", fun=SketchPen.move_counter_clockwise)
screen.onkey(key="d", fun=SketchPen.move_clockwise)
screen.onkey(key="c", fun=SketchPen.clear_drawings)

screen.exitonclick()