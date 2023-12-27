#!/usr/bin/env python3
import time
import turtle


def shape_one(turtle: turtle.Turtle, *, cur_size: float, min_size: float) -> None:
    if cur_size < min_size:
        return

    turtle.forward(cur_size)
    turtle.left(30)
    shape_one(turtle, cur_size=cur_size / 2, min_size=min_size)
    turtle.right(60)
    shape_one(turtle, cur_size=cur_size / 2, min_size=min_size)
    turtle.left(30)
    turtle.back(cur_size)


def shape_two(turtle: turtle.Turtle, *, cur_size: float, min_size: float) -> None:
    if cur_size < min_size:
        t.forward(min_size)
    else:
        shape_two(turtle, cur_size=cur_size / 3, min_size=min_size)
        t.left(60)
        shape_two(turtle, cur_size=cur_size / 3, min_size=min_size)
        t.right(120)
        shape_two(turtle, cur_size=cur_size / 3, min_size=min_size)
        t.left(60)
        shape_two(turtle, cur_size=cur_size / 3, min_size=min_size)


if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    # Give turtle enough space
    t.penup()
    t.back(200)
    t.pendown()

    shape_one(t, cur_size=100.0, min_size=5.0)
    shape_two(t, cur_size=200.0, min_size=5.0)

    # Pause for reflection
    time.sleep(10)
