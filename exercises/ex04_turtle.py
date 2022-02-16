"""Starry Day."""

__author__ = "730233362"

import random
from turtle import Turtle, colormode, done
colormode(255)


def draw_star(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a star."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 3:
        a_turtle.begin_fill()
        a_turtle.forward(width)
        a_turtle.right(170)
        a_turtle.forward(width)
        a_turtle.left(300)
        a_turtle.forward(width)
        a_turtle.right(170)
        a_turtle.forward(width)
        a_turtle.left(300)
        a_turtle.forward(width)
        a_turtle.right(170)
        a_turtle.forward(width)
        a_turtle.left(300)
        a_turtle.forward(width)
        a_turtle.right(170)
        a_turtle.forward(width)
        a_turtle.left(300)
        a_turtle.end_fill()
        i = i + 1


MAX_SPEED: int = 0


def main() -> None: 
    """The entrypoint of my scene."""
    vincent: Turtle = Turtle()
    vincent.color("yellow", "yellow")
    vincent.speed(MAX_SPEED)
    i: int = 0
    while i < 5:
        draw_star(vincent, random.randint(-200, 200), random.randint(-200, 200), random.randint(0, 150))
        i = i + 1
    done()


if __name__ == "__main__":
    main()