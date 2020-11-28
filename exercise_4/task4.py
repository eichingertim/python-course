import random

def calc_a_b_c():
    a_ = random.uniform(0, 1)
    b_ = 1 - a_

    a_or_b = random.uniform(0, 1)

    if a_or_b >= 0.5:
        a_ = random.uniform(0, a_)
    else:
        b_ = random.uniform(0, b_)

    c_ = 1 - a_ - b_
    return (a_, b_, c_)


counter = 0
tries = 100000

for i in range(tries):
    a, b, c = calc_a_b_c()
    if a + b > c and a + c > b and b + c > a:
        counter += 1

print("Wahrscheinlichkeit: {:.3f}".format(counter / tries))