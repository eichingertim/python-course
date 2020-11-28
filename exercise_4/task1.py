vector_a = [3, 2, 1, 5, 7, 2, -1]
vector_b = [-7, 3, 7, 5, 6, 8, 1]

skalarproduct = 0

for i in range(len(vector_a)):
    skalarproduct += vector_a[i] * vector_b[i]

print(skalarproduct)