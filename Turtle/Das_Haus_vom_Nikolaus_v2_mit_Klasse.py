# https://docs.python.org/3.13/library/turtle.html
from random import randint
import turtle  # Bestandteil von tkinter

count = 100
height = 1080
width = 1080


# Klassen
class Haus:
    def __init__(self, x=0, y=0, a=100, color=(128,128,128), size=3):
        self.x = x
        self.y = y
        self.a = a
        self.color = color
        self.size = size

    def zeichnen(self):
        turtle.pencolor(self.color)
        turtle.pensize(self.size)
        turtle.teleport(self.x, self.y)
        turtle.goto(self.x + self.a, self.y)
        turtle.goto(self.x, self.y + self.a)
        turtle.goto(self.x + self.a, self.y + self.a)
        turtle.goto(self.x, self.y)
        turtle.goto(self.x, self.y + self.a)
        turtle.goto(self.x + self.a / 2, self.y + self.a + self.a / 2)
        turtle.goto(self.x + self.a, self.y + self.a)
        turtle.goto(self.x + self.a, self.y)

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
    haus = Haus(x, y, a, color, size)   # .zeichnen() ggf. init und method in einer Zeile
    haus.zeichnen()
    count -= 1

# Programmende
print("Fertig!")
turtle.teleport(0, 0)
turtle.pencolor(255, 0, 0)
turtle.write("Fertig!", align="center", font=("Arial", 32, "bold"))
turtle.hideturtle()
turtle.done()
