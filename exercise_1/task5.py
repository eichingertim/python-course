TABLE = [[34, 234, 2],
        [3, 234, 4234],
        [6, 234, 8],
        [9, 1340, 11]]

def input_calculate():
    search = input("Gib die Nummer ein die du suchen willst: ")
    
    counter = 0

    for i in range(len(TABLE)):
        for j in range(len(TABLE[0])):
            if (counter == int(search)):
                print('Zeile: {}, Spalte: {}'.format(i+1, j+1))
            counter += 1

input_calculate()