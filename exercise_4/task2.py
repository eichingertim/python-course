stringVar = "Hallo mein Name ist Tim"

table = dict()

for char in stringVar:
    try: 
        table[char] += 1
    except KeyError:
        table[char] = 1

print(table)