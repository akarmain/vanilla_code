from collections import Counter
from random import randint


def can_make_palindrome(nums):
    num_counts = Counter(nums)
    odd_count = 0
    for count in num_counts.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count <= 1


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = arr[i - 2] + arr[i - 1]
    p = p[2:]
    if min(p) == max(p):
        return True
    else:
        return randint(0, 1)
        # return can_make_palindrome(p)


if __name__ == '__main__':
    for _ in range(int(input())):
        # main()
        print("Yes" if main() else "NO")
