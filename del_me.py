import sys

sys.setrecursionlimit(9999999) # для рекурсии

# 8
from itertools import product
p = product('0123456789ABC', repeat=5)
ans = 0
for s in p:
    if s[0] != '0' and (s.count('7') == 1) and (...):
        ans += 1
print(ans)

print(*(f"A{i}" for i in range(5)), end="")

# 13
from ipaddress import ip_network

for i in ip_network('10.48.96.0/255.255.240.0', 0):
    print(f"f{i:b}")

# 25
from fnmatch import *
def main_25():
    for x in range(0, 10 ** 10, 2024):
        if fnmatch(str(x), '10*2024?'):
            print(x, x // 2024)


# пятиричная запись числа
def to_5(n):
    n_5 = ''
    while n > 0:
        n_5 = n_5 + str(n % 5)
        n //= 5
    return int(n_5, 5)

# теория
from itertools import permutations
data = [1, 2, 3]
result = permutations(data, 2)
print("Перестановки из [1, 2, 3] по 2 элемента:")
for item in result:
    print(item)

# теория
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = combinations_with_replacement(data, 2)
print("\nКомбинации с повторениями из ['A', 'B', 'C'] по 2 элемента:")
for item in result:
    print(item)


# черепаха 6

from turtle import *
tracer(0)
left(90)
speed(10000)
k = 30
for _ in range(7):
    forward(10*k)
    left(120)
pu()
for x in range(-10 * k, 10 * k):
    for y in range(-10 * k, 10 * k):
        setpos(x * k, y * k)
        dot(2, 'red')
done()

# 27
def centroid(cluster: list[int, int]) -> (int, int):
    x_centr, y_centr = 0, 0
    minim = float('inf')
    for i, (x1, y1) in enumerate(cluster):
        res = sum(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 for x2, y2 in cluster)
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr