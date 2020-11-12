TABLE = [[34, 234, 2],
        [3, 234, 4234],
        [6, 234, 8],
        [9, 1340, 11]]

def print_table():
    for i in range(len(TABLE)):
        for j in range(len(TABLE[0])):
            print(" " + str(TABLE[i][j]), end=",")
        print()
def input_calculate():
    search = input("Gib die Nummer ein die du suchen willst: ")

    col = 1
    row = 1
    counter = 0
    found = False
    for i in range(len(TABLE)):
        for j in range(len(TABLE[0])):
            if (counter == int(search)):
                print("Zeile: " + str(row) + ", Spalte " + str(col))
                found = True
                break
            counter += 1
            col += 1
        if (found == True):
             break
        row += 1
        col = 1

print_table()
input_calculate()