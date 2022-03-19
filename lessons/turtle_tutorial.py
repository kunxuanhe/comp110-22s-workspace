from turtle import Turtle, colormode, done

leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -130)
leo.pendown()
colormode(255)
leo.color(10, 231, 229)
leo.speed(10)

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()

# bob: Turtle = Turtle()
# bob.penup()
# bob.goto(-150, -130)
# bob.pendown()
# colormode(255)
# bob.color(1, 15, 15)
# bob.speed(100)

# side_length: float = 300
# i: int = 0
# while (i < 100):
#     bob.forward(side_length)
#     bob.left(121)
#     i = i + 1
#     side_length = side_length * 0.97

done()
