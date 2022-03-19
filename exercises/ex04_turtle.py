"""TODO: Describe your scene program."""

__author__ = "730528983"

from turtle import Turtle, colormode, done 


def draw_square(t: Turtle, x: float, y: float, width: float) -> None:
    """I will show a flag of China by using Turtle and the flag contains five stars with yellow color."""
    colormode(255)
    t.hideturtle()
    t.speed(9)
    t.color(10, 200, 222)
    t.fillcolor("red")
    t.penup()
    t.goto(x, y)
    t.goto(-400, 300)
    t.pendown()
    width = 1000.9

    t.begin_fill()
    i: int = 0
    while (i < 2):
        t.forward(width)
        t.right(90)
        t.forward(width)
        t.right(90)
        i += 1
    t.end_fill()


def star1(t: Turtle, x: float, y: float, width: float) -> None:
    """This is the first and the biggest yellow star on the flag. It is located at the left corner of the red square."""
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.penup()
    t.goto(-300, 200)
    t.pendown()
    t.begin_fill()
    width = 80.9

    i: int = 0
    while (i < 5):
        t.forward(width)
        t.left(72)
        t.forward(width)
        t.right(144)
        i += 1
    t.end_fill()


def star2(t: Turtle, x: float, y: float, width: float) -> None:
    """This is the second samll yellow satr on the flag. It is around the biggest yellow star."""
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.penup()
    t.goto(-50, 270)
    t.pendown()
    t.begin_fill()
    t.right(30)
    width = 20.9

    i: int = 0
    while (i < 5):
        t.forward(width)
        t.left(72)
        t.forward(width)
        t.right(144)
        i += 1
    t.end_fill()


def star3(t: Turtle, x: float, y: float, width: float) -> None:
    """This is the third small yellow star on the flag. It is around the biggest yellow star."""
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.penup()
    t.goto(0, 200)
    t.pendown()
    t.begin_fill()
    width = 20.9

    i: int = 0
    while (i < 5):
        t.forward(width)
        t.left(72)
        t.forward(width)
        t.right(144)
        i += 1
    t.end_fill()


def star4(t: Turtle, x: float, y: float, width: float) -> None:
    """This is the fourth small yellow star on the flag. It is around the biggest yellow star."""
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.begin_fill()
    t.left(30)
    width = 20.9

    i: int = 0
    while (i < 5):
        t.forward(width)
        t.left(72)
        t.forward(width)
        t.right(144)
        i += 1
    t.end_fill()


def star5(t: Turtle, x: float, y: float, width: float) -> None:
    """This is the last small yellow star on the flag. It is around the biggest yellow star."""
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.penup()
    t.goto(-55, 40)
    t.pendown()
    t.begin_fill()
    t.right(30)
    width = 20.9

    i: int = 0
    while (i < 5):
        t.forward(width)
        t.left(72)
        t.forward(width)
        t.right(144)
        i += 1
    t.end_fill()


def main() -> None:
    """The foundation of my scene. It will include a red square and five locations for yellow star."""
    ertle: Turtle = Turtle()
    draw_square(ertle, -350, 300, 100)
    star1(ertle, -300, 200, 50)
    star2(ertle, -50, 270, 50)
    star3(ertle, 0, 200, 50)
    star4(ertle, 0, 100, 50)
    star5(ertle, -55, 40, 50)

    done()


if __name__ == "__main__":
    main()