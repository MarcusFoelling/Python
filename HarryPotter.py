from random import choice, shuffle

spells = (
    ("Accio", "Beschwört ein Objekt herbei"),
    ("Aguamenti", "Erzeugt Wasser aus dem Zauberstab"),
    ("Alohomora", "Öffnet verriegelte Türen"),
    ("Aparecium", "Macht unsichtbare Tinte sichtbar"),
    ("Avada Kedavra", "Tötet sofort (unverzeihlicher Fluch)"),
    ("Avis", "Beschwört einen Schwarm Vögel"),
    ("Colloportus", "Verschließt Türen magisch"),
    ("Confringo", "Lässt Dinge explodieren"),
    ("Confundo", "Verwirrt eine Person"),
    ("Crucio", "Verursacht Angst und unerträgliche Schmerzen (unverzeihlicher Fluch)"),
    ("Deletrius", "Löscht die Spuren eines Zaubers"),
    ("Densaugeo", "Lässt die Zähne wachsen"),
    ("Depulso", "Schiebt ein Objekt weg"),
    ("Descendo", "Lässt Dinge nach unten fallen"),
    ("Diffindo", "Schneidet oder reißt Dinge auf"),
    ("Dissendium", "Öffnet einen Geheimgang"),
    ("Draconifors", "Verwandelt ein Objekt in eine kleine Drachenfigur"),
    ("Duro", "Verwandelt ein Objekt in Stein"),
    ("Engorgio", "Lässt Dinge oder Lebewesen wachsen"),
    ("Episkey", "Heilt kleinere Verletzungen"),
    ("Evanesco", "Lässt Dinge verschwinden"),
    ("Expecto Patronum", "Beschwört einen Patronus, Schutz gegen Dementoren"),
    ("Expelliarmus", "Entwaffnet das Ziel"),
    ("Expulso", "Löst eine Explosion an einem Objekt aus"),
    ("Ferula", "Erzeugt Bandagen und Schienen"),
    ("Fidelius", "Verbirgt ein Geheimnis in einem Geheimniswahrer"),
    ("Finite", "Beendet laufende Zaubereffekte"),
    ("Finite Incantatem", "Beendet Magie im Allgemeinen"),
    ("Flagrate", "Erzeugt leuchtende Linien in der Luft"),
    ("Flipendo", "Rückstoßzauber (schleudert weg, vor allem in Spielen)"),
    ("Fumos", "Erzeugt Rauch als Tarnung"),
    ("Furnunculus", "Lässt Furunkel auf der Haut wachsen"),
    ("Geminio", "Dupliziert ein Objekt"),
    ("Glacius", "Gefriert Wasser oder Gegenstände (meist Spiele)"),
    ("Homenum Revelio", "Enthüllt versteckte Menschen"),
    ("Impedimenta", "Hält das Ziel auf oder verlangsamt es"),
    ("Imperio", "Nimmt Kontrolle über das Ziel (unverzeihlicher Fluch)"),
    ("Impervius", "Macht Dinge wasserabweisend"),
    ("Incarcerous", "Lässt Seile erscheinen, die das Ziel fesseln"),
    ("Incendio", "Erzeugt Feuer"),
    ("Langlock", "Klebt die Zunge am Gaumen fest"),
    ("Legilimens", "Erlaubt das Eindringen in Gedanken (Legilimentik)"),
    ("Levicorpus", "Lässt das Ziel kopfüber schweben"),
    ("Liberacorpus", "Hebt Levicorpus auf"),
    ("Lumos", "Bringt die Zauberstabspitze zum Leuchten"),
    ("Lumos Maxima", "Kräftiges Licht am Zauberstab"),
    ("Mobiliarbus", "Bewegt (vor allem) Möbelstücke"),
    ("Mobilicorpus", "Bewegt einen gelähmten Körper"),
    ("Morsmordre", "Beschwört das Dunkle Mal in den Himmel"),
    ("Muffliato", "Verhindert, dass andere ein Gespräch belauschen können"),
    ("Nox", "Löscht das Licht der Zauberstabspitze aus"),
    ("Obliviate", "Löscht oder verändert Erinnerungen"),
    ("Oppugno", "Lässt Tiere (meist Vögel) das Ziel attackieren"),
    ("Orchideous", "Lässt Blumen erscheinen"),
    ("Petrificus Totalus", "Ganzkörperklammer, lähmt das Ziel vollständig"),
    ("Periculum", "Rote Funken als Notsignal"),
    ("Portus", "Verwandelt ein Objekt in einen Portschlüssel"),
    ("Prior Incantato", "Zeigt den zuletzt ausgeführten Zauber eines Zauberstabs"),
    ("Protego", "Schützt mit einem Zauberschild vor Angriffen"),
    ("Protego Totalum", "Stellt einen großflächigen magischen Schutzschild her"),
    ("Quietus", "Macht die eigene Stimme wieder leise"),
    ("Reducto", "Zerstört oder zertrümmert Gegenstände"),
    ("Relashio", "Lässt das Ziel los/löst Fesseln"),
    ("Rennervate", "Weckt jemand aus der Bewusstlosigkeit"),
    ("Reparo", "Repariert zerbrochene Gebilde und Gegenstände"),
    ("Repello Muggletum", "Hält Muggel fern"),
    ("Rictusempra", "Kitzelzauber, versetzt das Ziel in Kitzelkrämpfe"),
    ("Riddikulus", "Verwandelt den Irrwicht in etwas Lächerliches"),
    ("Scourgify", "Reinigungszauber"),
    ("Sectumsempra", "Verursacht schwere Schnittwunden"),
    ("Serpensortia", "Lässt eine Schlange aus dem Zauberstab erscheinen"),
    ("Silencio", "Macht das Ziel stumm"),
    ("Sonorus", "Verstärkt die Stimme"),
    ("Stupefy", "Betäubt das Ziel, setzt es außer Gefecht"),
    ("Tarantallegra", "Zwingt die Beine des Ziels, wild zu tanzen"),
    ("Tergeo", "Saugt Flüssigkeiten und Verschmutzungen auf"),
    ("Waddiwasi", "Schießt kleine Gegenstände durch die Luft"),
    ("Wingardium Leviosa", "Lässt Objekte schweben bzw. schweben und bewegen"),
)

while True:
    question = choice(spells)
    answers = [
        question[0],
        choice(spells)[0],
        choice(spells)[0],
        choice(spells)[0],
    ]
    shuffle(answers)

    print("-" * 80)
    print(f"\nWelcher Zauberspruch: {question[1]}")
    print(
        f"\nA) {answers[0]}     B) {answers[1]}     C) {answers[2]}     D) {answers[3]}"
    )
    userinput = input().lower()

    match userinput:
        case "a":
            useranswer = answers[0]
        case "b":
            useranswer = answers[1]
        case "c":
            useranswer = answers[2]
        case "d":
            useranswer = answers[3]
        case _:  # falls die Eingabe nicht passend ist
            exit()

    if useranswer == question[0]:
        print("Richtig! Du bist auf dem Weg ein gute Hexe oder Zauberer zu werden!\n")
    else:
        print(f"Leider falsch! Die Antwort ist {question[0]}.\n")
    print("*" * 80)
