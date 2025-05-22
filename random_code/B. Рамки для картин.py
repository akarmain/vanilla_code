def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    k = [0] * 101
    ans = 0
    for i in arr:
        k[i] += 1

    for item in k:
        ans += item // 2

    return ans // 2


if __name__ == '__main__':
    print(main())



"""


3 4

xi yj
templates1.ipynb 2 - templates1.ipynb 2 +
3 4 - 5 4 - 
2 4 - 2 4 +


i j
5 4
templates1.ipynb templates1.ipynb



"""