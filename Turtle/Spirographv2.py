import turtle
import colorsys

# Variables vorbereiten und Default Values setzen
color = [0, 0, 0]
distance_from_center = 80
hue = 0                         # beschreibt das Farbspektrum von 0 bis 1
max_circle = 120
radius = 100

# Bildschirm vorbereiten
screen = turtle.Screen()
screen.bgcolor("black")

# Schildkröte vorbereiten
t = turtle.Turtle()
t.speed(0)          # maximale Geschwindigkeit
t.width(2)          # Linienbreite

for i in range(max_circle):
    # Farbwahl (Regenbogeneffekt)
    hue = i / max_circle
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)

    # Kreis und Rotation
    t.penup()
    t.goto(0, 0)
    t.forward(distance_from_center)
    t.left(360 / max_circle)
    t.pendown()
    t.circle(radius, 90)        # Viertelkreis (90 Grad)
    t.circle(radius/4, 90)      # Viertelkreis (90 Grad) (1/4)
    t.circle(radius, 90)        # Viertelkreis
    t.circle(radius/4, 90)      # Viertelkreis (90 Grad)
    
    # optional:
    # print(f"i = {i}    hue = {hue}     color = {color}")

turtle.done()
