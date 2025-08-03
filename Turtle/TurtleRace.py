import turtle
from time import sleep

colors = ["red", "green"]
end_x = 300  # Zielposition auf x-Achse
players = []
start_y = -20

def check_winner():
    for player in players:
        if player.xcor() >= end_x:
            turtle.onkey(None, "a")
            turtle.onkey(None, "#")

            # Siegeranzeige
            countdown_turtle.clear()
            worker_turtle.teleport(countdown_turtle.xcor(), countdown_turtle.ycor())
            worker_turtle.color(player.color()[0])
            worker_turtle.write(f"{player.color()[0].capitalize()} gewinnt!", align="center", font=("Arial", 28, "bold"))
            print(f"{player.color()[0].capitalize()} gewinnt!")

def player1_move():
    players[0].forward(10)
    check_winner()

def player2_move():
    players[1].forward(10)
    check_winner()


# Bildschirm vorbereiten
turtle.title("Turtle Race")
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Ziellinie zeichnen
worker_turtle = turtle.Turtle()
worker_turtle.hideturtle()
worker_turtle.teleport(end_x, -100)
worker_turtle.left(90)
worker_turtle.forward(200)

# Spielregeln schreiben
worker_turtle.teleport(0, -150)
worker_turtle.write("Spieler 1 nutzt die Taste A, Spieler 2 nutzt die Taste #, möge der bessere Spieler gewinnen!", align="center", font=("Arial", 18, "bold"))

# Rennteilnehmer erstellen und aufstellen
for color in colors:
    player_turtle = turtle.Turtle()
    player_turtle.color(color)
    player_turtle.shape("turtle")
    player_turtle.penup()
    player_turtle.goto(-300, start_y)
    player_turtle.pendown()
    players.append(player_turtle)
    start_y += 40

# Countdown
countdown_turtle = turtle.Turtle()
countdown_turtle.hideturtle()
countdown_turtle.teleport(0, 100)
for i in range(3, 0, -1):       # Countdown zählt rückwärts
    countdown_turtle.clear()
    countdown_turtle.write(f"{i}", align="center", font=("Arial", 36, "bold"))
    sleep(1)
countdown_turtle.clear()
countdown_turtle.write("Los!", align="center", font=("Arial", 32, "bold"))

# Das Rennen starten
turtle.onkey(player1_move, "a")     # Player1 Taste zuweisen
turtle.onkey(player2_move, "#")     # Player2 Taste zuweisen
turtle.listen()                     # Tastatur Abfragen aktivieren
turtle.mainloop()                   # Fortlaufende Schleife, damit Tastaturabfrage ausgeführt wird
