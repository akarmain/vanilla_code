## Задание 1


from itertools import *

# из каждой строки выписываем города, с которыми соединяется строчка
tab = '57 457 46 236 12 348 128 67'.split()

# выписываем все соединения из города 457
k = int(tab[1])
ans = []
for i in range(0, len(tab), 2):
    if int(tab[i]) == k:
        ans.append(int(tab[i+1]))
print(*ans)


## Задание 2

"""
A and B    # Логическое И (конъюнкция)
A or B     # Логическое ИЛИ (дизъюнкция)
not A      # Логическое НЕ (отрицание)
A != B     # Логическое исключающее ИЛИ (XOR)
A == B     # Логическое равенство (эквиваленция)
A → B      # Эквивалент импликации (если A, то B) not A or B  
"""



print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x <= y) and (z == (w <= x)) and (not w) == 1:
                    print(x, y, z, w)


def fun(x, y, z, w):
    return (x <= y) and (z == (w <= x)) and (not w)

# буквы - это пробелы в таблице
from itertools import product, permutations
for a, b, c, d, e, f, g in product((0, 1), repeat=7):
    table = ((0, a, b, 0, 1),
             (1, 0, c, d, 1),
             (e, 1, f, g, 1))
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(fun(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)


## Задание 5


for i in range(9999, 999, -1):
    ns = str(i) # создаем строку из числа, чтобы брать оттуда цифры
    x = int(ns[0]) + int(ns[1])
    y = int(ns[1]) + int(ns[2])
    z = int(ns[2]) + int(ns[3])
    sums = sorted([x, y, z])
    r = str(sums[1]) + str(sums[2])
    if r == '1115':
        print(i)
        break # нашли наибольший ответ, дальше не смотрим



for n in range(1000):
    r = f'{n:b}'
    if n % 2 == 0:
        r += '10'
    else:
        r += '11'
    r = int(r, 2)
    if r > 105:
        print(n)
        break


## Задание 6


from turtle import *

tracer(0)  # рисунок сразу появляется
lt(90)  # на ось ординат
screensize(2000, 2000) # полосы прокрутки
k = 20  # коэффициент масштаба
for i in range(3):
    fd(11 * k)
    rt(90)
    fd(24 * k)
    rt(90)
up()
fd(2 * k)
right(90)
for i in range(2):
    fd(6 * k)
    rt(90)
    fd(22 * k)
    rt(90)
up()

fd(1 * k)
rt(90)
for i in range(3):
    fd(6 * k)
    lt(90)
    fd(9 * k)
    lt(90)
done()


## Задание 8


from itertools import *
s = 1*'3'
ans = []
for n in range(1, 100):
    s += s[-1]
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        s = s + s[-1]
    if s.count('3') == 7:
        ans.append(n)
print(max(ans))


## Задание 9


f = open("9")
cnt = 0
for s in f:
    # строки в числа
    m = [int(x) for x in s.split()]
    m.sort()
    # первое условие выполнимо только с такими парами
    if (m[0] * m[3]) == (m[1] * m[2]):
        # второе условие
        if m[-2]**2 > m[0] * m[3]:
            cnt += 1
print(cnt)


## Задание 11


from math import *

for n in range(1, 1000):
    i = ceil(log2(n))
    ser = ceil(377 * i / 8)
    if 23155 * ser > 5536 * 1024:
        print(n)
        break


from math import *

n = 10 + 26 + 496  # мощность алфавита
i = ceil(log2(n))

for l in range(1, 1000):
    id = ceil(l * i / 8) # байт на айди
    if id * 725 > 353 * 1024:
        print(l)
        break


## Задание 12


s = 111 * "3"
while "33333" in s or "1111" in s:
    if "33333" in s:
        s = s.replace("33333", "111", 1)
    else:
        s = s.replace("111", "33", 1)
print(s.count("1"))

ans = []
for x in range(10): # обозначим за х количество единиц
    for y in range(1, 10):     # за y - количество двоек
        s = "1" * x + "2" * y
        while "1" in s or "2" in s:
            s = s.replace("1", "22", 1)
            s = s.replace("2", "3", 1)
        if s == "333333":
            ans.append(x)
print(max(ans))


## Задание 13


from ipaddress import *

# создаем сеть
n = ip_network('211.46.0.0/255.255.128.0', 0)
cnt = 0
for ip in n:
    s = f'{ip:b}'  # заполняем ведущими нулями
    if (s.count('1') % 4 == 0) and (s[-2:] == '11'):
        cnt += 1
print(cnt)


from ipaddress import *

net = ip_network("143.168.72.213/255.255.255.240", 0)
print(net[-2])


## Задание 14


# развернули строку, так как нужен наибольший икс
s = "011010000011"[::-1]
x = int(s, 2)
cnt = 0
while x != 0:
    cnt += 1
    if x % 2 == 0:
        x = x // 2
    else:
        x = int('1' + format(x, 'b')[1:], 2)
print(cnt)


from functools import *
memo = {}
def f(s):
    if s % 2 == 0:
        return f(s // 2)
    else:
        s = int('1' + format(s, 'b')[1:], 2)
        return f(s) if s % 2 == 0 else s

cnt = 0
a = 0
for i in range(10**6, 10**6+100):
    x = i
    while x != 0 and x % 2 == 0:
        x = x // 2
        cnt += 1
    if x > 0:
        a = i
print(cnt, a)


## Задание 15


# ∧
def f(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        return x//2
    return f(x-1) + f(x-2)

cnt = 0
a = 1
while f(a) < 1000:
    cnt += 1
    a += 1
print(cnt)

print(a)


## Задание 16


from functools import *
memo = {}
def f(x):
    if x < 6:
        return 1
    if x not in memo:
        memo[x] = f(x-1) + f(x-3) + f(x-4)
    return memo[x]

cnt = 0
for i in range(20, 100):
    if f(i) >= 100:
        cnt += 1
        print(i, f(i))


## Задание 17


f = open('17.txt')
ans = []
for s in f:
    m = [int(x) for x in s.split()]
    if max(m) > 150:
        ans.append(max(m))
print(len(ans), max(ans))


## Задание 19


def f(s, m):  # s-количество камней, m-осталось ходов до конца игры
    if s <= 19: return m % 2 == 0 # условие победы
    if m == 0: return 0
    h = [f(s - 2, m - 1), f(s - 5, m - 1), f(s // 3, m - 1)] # ходы
    return any(h) if m % 2 != 0 else all(h)

print('19)', min([s for s in range(20, 100) if f(s, 2)]))


## Задание 20


def f(s, m):  # s-количество камней, m-осталось ходов до конца игры
    if s <= 19: return m % 2 == 0 # условие победы
    if m == 0: return 0
    h = [f(s - 2, m - 1), f(s - 5, m - 1), f(s // 3, m - 1)] # ходы
    return any(h) if m % 2 != 0 else all(h)

print('19)', min([s for s in range(20, 100) if f(s, 2)]))
print('20)', *[s for s in range(20, 100) if f(s, 3) and (not f(s, 1))])
def f(a, b, m):  # a,b - количества камней в кучах, m-осталось ходов до конца
# игры
    if a+b >= 65: return m % 2 == 0 # условие победы
    if m == 0: return 0
    h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*3, b, m-1), f(a, b*3, m-1)] # ходы
    return any(h) if m % 2 != 0 else all(h)
    # return any(h) if m % 2 != 0 else any(h) #ДЛЯ 19 НОМЕРА!!!

# print('19)', *[s for s in range(1, 59) if f(6, s, 2)])
print('20)', *[s for s in range(1, 59) if f(6, s, 3) and (not f(6, s, 1))])


## Задание 21


def f(s, m):  # s-количество камней, m-осталось ходов до конца игры
    if s <= 19: return m % 2 == 0 # условие победы
    if m == 0: return 0
    h = [f(s - 2, m - 1), f(s - 5, m - 1), f(s // 3, m - 1)] # ходы
    return any(h) if m % 2 != 0 else all(h)

print('19)', min([s for s in range(20, 100) if f(s, 2)]))
print('20)', *[s for s in range(20, 100) if f(s, 3) and (not f(s, 1))])
print('21)', min([s for s in range(20, 100) if f(s, 4) and (not f(s, 2))]))
def f(a, b, m):  # a,b - количества камней в кучах, m-осталось ходов до конца



# игры
    if a+b >= 65: return m % 2 == 0 # условие победы
    if m == 0: return 0
    h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*3, b, m-1), f(a, b*3, m-1)] # ходы
    return any(h) if m % 2 != 0 else all(h)
    # return any(h) if m % 2 != 0 else any(h) #ДЛЯ 19 НОМЕРА!!!

# print('19)', *[s for s in range(1, 59) if f(6, s, 2)])
print('20)', *[s for s in range(1, 59) if f(6, s, 3) and (not f(6, s, 1))])
print('21)', *[s for s in range(1, 59) if f(6, s, 4) and (not f(6, s, 2))])


## Задание 23


def f(s, e):
    if s > e or s == 20:
        return 0
    if s == e:
        return 1
    return f(s + 1, e) + f(s + (s + 1), e)

print(f(3, 12) * f(12, 28))


def f(s, e):
    if s < e or s == 24:
        return 0
    if s == e:
        return 1
    return f(s - 1, e) + f(s - 6, e) + f(s // 2, e)
print(f(34, 29) * f(29, 19) * f(19, 6))


## Задание 25


from fnmatch import *
for i in range(1917, 10**10, 1917):
    if fnmatch(str(i), '3?12?14*5'):
        print(i, i // 1917)


## Задание 27

x2, y2 = 0, 0
for _ in range(100):
    A = randint(1, 5)
    B = randint(1, 5)
    if (x == 2*A) and (y == 2*B):
        x2 += x
        y2 += y
print(int(px2), int(py2))
