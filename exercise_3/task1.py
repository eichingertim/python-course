import math
import cmath

def read_in_variable(text):
    variable = ""
    while (not variable.isdigit()):
        variable = input(text)
        try:
            variable = float(variable)
            return variable
        except ValueError:
            print("This was not a number. Try again!")

def calculate_zero_points(a, b, c, is_complex):
    x1, x2 = [0,0]
    if is_complex:
        x1 = ((-b) + cmath.sqrt(b*b-4*a*c))/(2*a)
        x2 = ((-b) - cmath.sqrt(b*b-4*a*c))/(2*a)
    else:
        x1 = ((-b) + math.sqrt(b*b-4*a*c))/(2*a)
        x2 = ((-b) - math.sqrt(b*b-4*a*c))/(2*a)
    return (x1, x2)

a = read_in_variable("Enter a digit for a: ")
b = read_in_variable("Enter a digit for b: ")
c = read_in_variable("Enter a digit for c: ")

try:
    zp = calculate_zero_points(a, b, c, False)
    print('Relle Zahlen x1: {:.3f}, x2: {:.3f}'.format(zp[0], zp[1]))
except ValueError:
    print("Keine Reelen Nullstellen vorhanden")

try:
    zpc = calculate_zero_points(a, b, c, True)
    print('Komplexe Zahlen x1: {:.3f}, x2: {:.3f}'.format(zpc[0], zpc[1]))
except ValueError:
    print("Keine Komplexen Nullstellen vorhanden")









