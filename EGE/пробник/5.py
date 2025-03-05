"""
URL: https://education.yandex.ru/ege/task/da1c175a-d87f-46d0-9211-35a2d2a5b554
"""


def algos(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        return int(b + b[-3:], 2)
    else:
        return int(b + bin((n % 5) * 5)[2:], 2)


def main():
    arr = []
    for i in range(1, 5120):
        r = algos(i)
        if r > 256:
            arr.append(i)

    return min(arr)


if __name__ == "__main__":
    print("ANS:", main())
