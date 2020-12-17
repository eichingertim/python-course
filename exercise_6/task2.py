import math

def calc_integral(func, acc=100):
    def integrate():
        area = 0.0
        rectangle_width = (1 - 0) / acc

        for i in range(acc):
            area += func(0 + (i * rectangle_width)) * rectangle_width
        return area
    return integrate


integral = calc_integral(math.sin, 10000)

print(integral())
