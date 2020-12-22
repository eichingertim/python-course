import random

class Spielfigur:

    base_points = 4
    points_surge = 1

    def __init__(self, name):
        self.name = name
        self.life_points = Spielfigur.base_points + random.randint(-Spielfigur.points_surge, Spielfigur.points_surge)
        self.strength_points = Spielfigur.base_points + random.randint(-Spielfigur.points_surge, Spielfigur.points_surge)
        self.intelligence_points = Spielfigur.base_points + random.randint(-Spielfigur.points_surge, Spielfigur.points_surge)
        self.speed_points = Spielfigur.base_points + random.randint(-Spielfigur.points_surge, Spielfigur.points_surge)
        self.charisma_points = Spielfigur.base_points + random.randint(-Spielfigur.points_surge, Spielfigur.points_surge)
        self.backpack = list()
        self.expose = False
        self.progress = 0

    def bearbeitePruefung(pruefung):


    def __str__(self):

        string = '''Name: {0}\n
                    Schritte zum Erfolg: {1}\n
                    Lebenspunkte: {2}\n
                    Stärkepunkte: {3}\n
                    Intelligenz: {4}\n
                    Geschwindigkeit: {5}\n
                    Charisma: {6}\n
                    Im Rucksack:\n'''.format(self.name, self.progress, self.life_points, self.strength_points, self.intelligence_points, self.speed_points, self.charisma_points)

        for gegenstand in self.backpack:
            string += '* {0} ({1} +{2}'.format(gegenstand.name, gegenstand.prop, gegenstand.points)

        return string