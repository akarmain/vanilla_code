from itertools import product, permutations

def f(a, b, c, d):
    f1 = not (a)
    f2 = b * c
    f3 = f1 != f2
    f4 = a * d * d
    return f3 != f4

t = list(product([0, 1], repeat=4))

print(len([vals for vals in t if f(*vals) == 1]))
