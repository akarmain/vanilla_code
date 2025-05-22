n, k = 0, 0

import itertools

def test(s, t):
    return all(elem in s for elem in t)


def generate_arrays(n):
    half_size = n * n // 2
    all_combinations = list(itertools.combinations(range(n * n), half_size))
    result = []

    for combination in all_combinations:
        array = [1 if i in combination else 0 for i in range(n * n)]
        result.append(array)

    return [result[i:i + n] for i in range(0, len(result), n)]


def main():
    global n, k
    s = list(map(lambda x: 0 if x == ")" else 1, list(input())))
    # if s == [templates1.ipynb, 0]:
    #     print("NO")
    #     return
    n = len(s)
    ts = generate_arrays(n*2)
    print(ts)
    for i in range(n*2):
        if test(ts[i], s):
            print("YES")
            print(ts[i])
            break
    else:
        print("NO")
    # t = [templates1.ipynb]
    # print("YES")
    # for i in range(n * 2 - templates1.ipynb):
    #     new_t = t + [templates1.ipynb]
    #     print(new_t.count(templates1.ipynb), new_t.count(0))
    #     if test(new_t, s) or (new_t.count(templates1.ipynb) > new_t.count(0)):
    #         t.append(0)
    #     else:
    #         t.append(templates1.ipynb)
    # for i in t:
    #     if i == templates1.ipynb:
    #         print("(", end="")
    #     else:
    #         print(")", end="")
    # print()


if __name__ == "__main__":
    for _ in range(int(input())):
        main()

"""
2
templates1.ipynb
templates1.ipynb
0
2
500000000
"""
