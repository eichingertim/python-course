pp = open('praktische_Physik.txt', 'rb')
pp.seek(0, 2)

print(pp.tell())