from random import randint

eingabe = 0
versuche = 0
zahl = randint(1, 9999)

print(
    f"\nLass uns Zahlenraten spielen, ich denke mir eine Zahl; meine Zahl hat {len(str(zahl))} Stellen."
)

while eingabe != zahl:
    versuche += 1
    while True:
        try:
            eingabe = int(input("\nRate meine Zahl: "))
            break
        except ValueError:
            print("Bitte nur Zahlen eingeben.")

    if eingabe == zahl:
        print(f"\nDas ist richtig, du hast {versuche} Versuche gebraucht!")
    elif eingabe < zahl:
        print("\nMeine Zahl ist größer.")
    elif eingabe > zahl:
        print("\nMeine Zahl ist kleiner.")
