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

    def bearbeitePruefung(self, pruefung, gegenstaende):
        decision = input(pruefung.TextEntscheidung + ': ')
        if decision.lower() == 'ja':
            print(pruefung.TextJa)
            sum = self.rollTheDice(self.getDiceNum(pruefung.AufgabeJaKategorie))

            if (sum > pruefung.AufgabeJaKosten):
                self.backpack.append(gegenstaende[random.randrange(0, len(gegenstaende))])
                self.progress += 1
                print('You got it!')
            else:
                self.life_points -= 1
                print('-1 lifepoints')
        else:
            print(pruefung.TextNein)
            sum = self.rollTheDice(self.getDiceNum(pruefung.AufgabeNeinKategorie))

            if (pruefung.AufgabeNeinKategorie == "expose"):
                self.expose = True
                print('You must expose')
            else:
                if (sum > pruefung.AufgabeNeinKosten):
                    self.backpack.append(gegenstaende[random.randrange(0, len(gegenstaende))])
                    self.progress += 1
                    print('You got it!')
                else:
                    self.life_points -= 1
                    print('-1 lifepoints')


    def rollTheDice(self, num):
        sum = 0

        for i in range(num):
            sum += random.randrange(1, 7)

        return sum

    def getDiceNum(self, category):
        d = {
            'life': self.life_points,
            'strength': self.strength_points,
            'intelligence': self.intelligence_points,
            'speed': self.strength_points,
            'charisma': self.charisma_points
        }
        return d[category]


    def __str__(self):

        string = '''
        Name: {0}
        Schritte zum Erfolg: {1}
        Lebenspunkte: {2}
        Stärkepunkte: {3}
        Intelligenz: {4}
        Geschwindigkeit: {5}
        Charisma: {6}
        Im Rucksack:
        '''.format(self.name, self.progress, self.life_points, self.strength_points, self.intelligence_points, self.speed_points, self.charisma_points)

        for gegenstand in self.backpack:
            string += '* {0} ({1} +{2})'.format(gegenstand.name, gegenstand.category, gegenstand.points)

        return string