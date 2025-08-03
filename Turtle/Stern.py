import turtle

t = turtle.Turtle()
t.speed(0)
t.color("blue")

for i in range(100):
    t.forward(i * 5)
    t.right(144)
    print(f"{i}\r", end="")

turtle.done()