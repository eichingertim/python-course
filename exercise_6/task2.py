import math

def integrate(func, start, stop, N): 

    area = 0.0
    rectangle_width = (stop - start) / N

    for i in range(N):
        area += func(start + (i * rectangle_width)) * rectangle_width
    
    return area

def calc_integral(func, end, acc=100):
    return integrate(func, 0, end, acc)

print(calc_integral(math.sin, 2*math.pi, 100000)) 
print(calc_integral(math.sin, 2*math.pi)) 