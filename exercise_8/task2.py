

zeilenumbrueche = 0
chars = 0
rows = 0
words = 0

with open("praktische_Physik.txt", "r") as pp:
    for line in pp:
        rows += 1
        for letter in line:
            chars += 1
            if letter == '\n':
                zeilenumbrueche += 1
            if letter == ' ':
                words += 1

print('Mit Zeilenumbrüchen: {0}'.format(chars))
print('Ohne Zeilenumbrüchen: {0}'.format(chars - zeilenumbrueche))
print('Zeilen: {0}'.format(rows))
print('Wörter: {0}'.format(words))