def nFach(func, N, x):

    if N == 1:
        return func(x)
    else:
        return func(nFach(func, N - 1, x))

        
def function(x):
    return x + 1
solution = nFach(function, 5, 0)

print(solution)