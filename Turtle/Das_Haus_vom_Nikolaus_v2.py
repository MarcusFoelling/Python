# https://docs.python.org/3.13/library/turtle.html
from random import randint
import turtle  # Bestandteil von tkinter

count = 100
height = 1080
width = 1080


# Funktionen
def Haus(x=0, y=0, a=100, color=[128, 128, 128], size=3):
    # Zeichnen
    turtle.pencolor(color)
    turtle.pensize(size)
    turtle.teleport(x, y)
    turtle.goto(x + a, y)
    turtle.goto(x, y + a)
    turtle.goto(x + a, y + a)
    turtle.goto(x, y)
    turtle.goto(x, y + a)
    turtle.goto(x + a / 2, y + a + a / 2)
    turtle.goto(x + a, y + a)
    turtle.goto(x + a, y)
    return None  # optional, mmn vergleicht None immer mit is, nicht mit ==


# Fenster einrichten
turtle.title("Haus vom Nikolaus")
turtle.shape("turtle")  # arrow, circle, ...
turtle.speed(0)  # 0 = sofort, 1 - 10 sehr schnell => help(turtle.speed)
turtle.colormode(255)  # erlaubt das definieren von RGB-Farbwerten
height = turtle.window_height()
width = turtle.window_width()

while count > 0:
    x, y, a = (
        randint(-width // 2, width // 2),  # float nicht erlaubt, integer wird erzwungen
        randint(-height // 2, height // 2),
        randint(1, 200),
    )
    color = [randint(0, 255), randint(0, 255), randint(0, 255)]
    size = randint(1, 10)
    Haus(x, y, a, color, size)
    count -= 1

# Programmende
print("Fertig!")
turtle.teleport(0, 0)
turtle.pencolor(255, 0, 0)
turtle.write("Fertig!", align="center", font=("Arial", 32, "bold"))
turtle.hideturtle()
turtle.done()
