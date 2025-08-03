# https://docs.python.org/3.13/library/turtle.html
import turtle  # Bestandteil von tkinter

# Hausparameter
a = 100  # Seitenlänge der Grundfläche in Pixel
# Startposition (unten links)
x, y = 0, 0  # 0,0 entspricht Mitte des Fensters

# Fenster einrichten
turtle.title("Haus vom Nikolaus")
turtle.shape("turtle")  # arrow, circle, ...
turtle.speed(3)  # 0 = sofort, 1 - 10 sehr schnell => help(turtle.speed)
turtle.pensize(3)

# Zeichnen
# turtle.penup()
# turtle.goto(x, y)
# turtle.pendown()
turtle.teleport(x, y)
turtle.goto(x + a, y)
turtle.goto(x, y + a)
turtle.goto(x + a, y + a)
turtle.goto(x, y)
turtle.goto(x, y + a)
turtle.goto(x + a / 2, y + a + a / 2)
turtle.goto(x + a, y + a)
turtle.goto(x + a, y)

# Programmende
turtle.hideturtle()
turtle.done()
