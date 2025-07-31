import turtle

grid_dimension = 300
block = grid_dimension / 3
columns = {
    'A': (-block * 1.5, -block * 0.5),  # links
    'B': (-block * 0.5, block * 0.5),   # mitte
    'C': (block * 0.5, block * 1.5),    # rechts
}
rows = {
    1: (block * 0.5, block * 1.5),      # oben
    2: (-block * 0.5, block * 0.5),     # mitte
    3: (-block * 1.5, -block * 0.5),    # unten
}
matrix = {
    1: {"A": None, "B": None, "C": None},
    2: {"A": None, "B": None, "C": None},
    3: {"A": None, "B": None, "C": None},
}
players = ("x", "o")
current_player = 0

def winner():
    t.teleport(0,0 - block * 2)
    t.color("red")
    t.write(players[current_player], align="center", font=("Arial", int(grid_dimension), "bold"))
    screen.onclick(None)

def check_winner():
    global current_player
    # Reihe
    for row in matrix.keys():
        if all(value == current_player for value in matrix[row].values()):
            winner()

    # Spalte
    for column in matrix[1].keys():
        if all(value == current_player for value in [row[column] for row in matrix.values() ]):
            winner()

    # Diagonale 1
    if all(value == current_player for value in (matrix[1]["A"], matrix[2]["B"], matrix[3]["C"])):
        winner()

    # Diagonale 2
    if all(value == current_player for value in (matrix[1]["C"], matrix[2]["B"], matrix[3]["A"])):
        winner()

    current_player = 1 - current_player  # Toggle zwischen 0 und 1

def mouse_click(x, y):
    column = None
    for col, (start, end) in columns.items():
        if start <= x <= end:
            column = col
            break
    row = None
    for r, (start, end) in rows.items():
        if start <= y <= end:
            row = r
            break
    if column and row:
        check_field(row, column)
        return row, column
    else:
        return None

def check_field(row, column):
    if matrix[row][column] is not None:     # Feld bereits belegt
        return
    t.teleport(columns[column][0]+block/2, rows[row][0]-block/8)
    farbe = ("blue", "green")[current_player]   # wechselt automatisch
    t.color(farbe)
    t.write(players[current_player], align="center", font=("Arial", int(block), "bold"))
    matrix[row][column] = current_player
    check_winner()

def draw_grid():
    for counter in range(1,3):
        t.teleport( -grid_dimension / 2, grid_dimension /2 - grid_dimension/3 * counter )
        t.forward(grid_dimension)
    t.right(90)
    for counter in range(1,3):
        t.teleport( -grid_dimension / 2 + grid_dimension/3 * counter, grid_dimension /2)
        t.forward(grid_dimension)

# Bildschirm vorbereiten
turtle.title("Tic Tac Toe")
screen = turtle.Screen()
screen.setup( grid_dimension * 1.5, grid_dimension * 1.5 )
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

draw_grid()
screen.onclick(mouse_click)

turtle.listen()                     # Mouse Events aktivieren
turtle.mainloop()                   # Fortlaufende Schleife
