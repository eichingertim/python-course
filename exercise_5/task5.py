import math

def integrate(func, start, stop, N): 

    area = 0.0
    rectangle_width = (stop - start) / N

    for i in range(N):
        area += func(start + (i * rectangle_width)) * rectangle_width
    
    return area


print(integrate(math.exp, 0, 1, 10000))