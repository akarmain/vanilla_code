# https://codeforces.com/contest/158/problem/B
#
def main():
    arr = list(input())
    arr_cop = arr[:]
    arr_cop.sort()
    for i, val in enumerate(arr):
        if val != arr_cop[i]:
            print(val, i, arr_cop[i], arr.index(arr_cop[i]))
            break
    print(arr)
    print(arr_cop)


if __name__ == '__main__':
    main()
