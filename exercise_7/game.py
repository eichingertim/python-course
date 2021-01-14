from pruefung import Pruefung
from gegenstand import Gegenstand
from spielfigur import Spielfigur
import random

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


while (player1.progress != 3 and player1.life_points != 0 and player2.progress != 3 and player1.life_points != 0):
    if not player1.expose:
        print("Player 1's turn\n")
        player1.bearbeitePruefung(pruefungen[random.randint(0, 2)], gegenstaende)
        print(player1)
    else: 
        player1.expose = False

    if not player2.expose:
        print("Player 2's turn\n")
        player2.bearbeitePruefung(pruefungen[random.randint(0, 2)], gegenstaende)
        print(player2)
    else: 
        player2.expose = False

if player1.progress == 3 and player2.progress == 3:
    print('Its a draw')
elif player1.progress == 3:
    print('Player 1 wins')
elif player2.progress == 3:
    print('Player 2 wins')
elif player1.life_points == 0:
    print('Player 2 wins')
elif player2.life_points == 0:
    print('Player 1 wins')

