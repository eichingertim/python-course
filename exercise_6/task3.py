import math

def calc_length(vec):
    return math.sqrt(vec[0]**2 + vec[1]**2)

def sort_list(data):
    new_list = list()
    for m in data:
        new_list.append(calc_length(m))

    for k in range(len(new_list)):
        x, i = min([(x, i) for (i, x) in enumerate(new_list[k:])])
        data[k], data[k + i] = data[k + i], data[k]

data = [(7, 3), (5, 5), (8, 2), (9, 1), (6, 4)]

print(data)

sort_list(data)

print(data)