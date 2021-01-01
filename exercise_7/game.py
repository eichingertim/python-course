from pruefung import Pruefung
from gegenstand import Gegenstand
from spielfigur import Spielfigur

pruefungen = [
    Pruefung("Aufgabe1", "TextJa", "TextNein", "strength", 2, "speed", 3),
    Pruefung("Aufgabe2", "TextJa", "TextNein", "intelligence", 1, "charisma", 2),
    Pruefung("Aufgabe3", "TextJa", "TextNein", "speed", 2, "intelligence", 4),
]

gegenstaende = [
    Gegenstand("Name1", "strength", 2),
    Gegenstand("Name2", "speed", 1),
    Gegenstand("Name3", "intelligence", 3),
]

player1 = Spielfigur("Tim")
player2 = Spielfigur("Timon")

print(player1)
