def f(s):
    arr = []
    for i in s:
        if i == '.':
            arr.append(0)
        else:
            arr.append(1)
    return arr


def main():
    arr = []
    code = [[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            [[1, 2, 2, 2, 2, 2, 2, 2, 2, 1]],
            [[1, 2, 3, 3, 3, 3, 3, 3, 2, 1]],
            [[1, 2, 3, 4, 4, 4, 4, 3, 2, 1]],
            [[1, 2, 3, 4, 5, 5, 4, 3, 2, 1]],
            [[1, 2, 3, 4, 5, 5, 4, 3, 2, 1]],
            [[1, 2, 3, 4, 4, 4, 4, 3, 2, 1]],
            [[1, 2, 3, 3, 3, 3, 3, 3, 2, 1]],
            [[1, 2, 2, 2, 2, 2, 2, 2, 2, 1]],
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]
    for i in range(10):
        arr.append(list(map(lambda s: f(s), input().split())))
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += arr[i][0][j] * int(code[i][0][j])

    return ans


if __name__ == '__main__':
    for i in range(int(input())):
        print(main())
