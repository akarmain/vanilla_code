"""
URL: https://education.yandex.ru/ege/task/488973a9-be8d-4241-960a-1e41c8dbfe94
"""
from itertools import count
from collections import Counter


def check_row(nums):
    counts = Counter(nums)
    if sorted(counts.values()) != [1, 1, 1, 2, 2]:
        return False

    if counts[max(nums)] != 1:
        return False
    return True


def main():
    ans = 0
    for l in open("../../imputs/EGE_9_ya_пробник.txt").readlines():
        inp = list(map(int, l.strip().split()))
        if check_row(inp):
            return sum(inp)


if __name__ == "__main__":
    print("ANS:", main())
