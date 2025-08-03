import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")

while True:
    eingabe = input("\n\nWann wurdest Du geboren? (TT.MM.JJJJ) ")
    try:
        geburtstag = datetime.strptime(eingabe, "%d.%m.%Y")
        break
    except ValueError:
        print("Eingabe fehlerhaft, bitte erneut versuchen.")

wochentag = geburtstag.strftime("%A")
print(f"\n\nDu wurdest an einem {wochentag} geboren.")

differenz = datetime.today() - geburtstag
print(f"Du bist bereits {differenz.total_seconds()} Sekunden alt")
print(f"oder {differenz.total_seconds() / 60} Minuten")
print(f"oder {differenz.total_seconds() / 60 / 60} Stunden")
print(f"oder {differenz.total_seconds() / 60 / 60 / 24} Tage")
print(f"oder {differenz.total_seconds() / 60 / 60 / 24 / 365} Jahre")
