A = []
A.append(A)

print(A)
print(len(A))
print(len(A[0]))
print(len(A[0][0]))
# print(len(A[0][0][0]))

A[0][0][0] = 1
print(A)

# Es zeigt immer auf die gleiche Referenz. 
# Wenn zur liste A wieder A hinzugefügt wird, hat die Referenzliste die Länge 1 und deswegen auch hat auch A[0] die länge 1, weil es A refernziert. Das könnte jetzt eweig so vortgeführt werden.
# Die Länge von A[0][0][0][0] wäre immer noch eins, da die immer die gleiche Referenz existiert.

# Wenn A[0][0] = 1 gesetzt wird, wir die Grundreferenz wieder verändert. das heißt sie hat nun den wert 1 und nicht mehr A. Deswegen würde nun len(A[0][0]) einen Fehler ergeben, da die lsite nur 1 als inhalt hat.