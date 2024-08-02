from turtle import Turtle


class SketchPen:

    _pen = Turtle()
    _pen.shape("arrow")

    @classmethod
    def move_forwards(cls):
        cls._pen.forward(10)

    @classmethod
    def move_backwards(cls):
        cls._pen.backward(10)

    @classmethod
    def move_counter_clockwise(cls):
        cls._pen.left(10)

    @classmethod
    def move_clockwise(cls):
        cls._pen.right(10)

    @classmethod
    def clear_drawings(cls):
        cls._pen.reset()
