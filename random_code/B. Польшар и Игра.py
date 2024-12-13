# РЕШИЛ НАУГАД 

def find_common_elements(arr1, arr2):
    common_elements = []
    elements_set = set(arr1)
    for x in arr2:
        if x in elements_set:
            common_elements.append(x)

    return common_elements


def main():
    n, m = map(int, input().split())
    arr_1 = []
    arr_2 = []
    for _ in range(n):
        arr_1.append(input().__hash__())
    for _ in range(m):
        arr_2.append(input().__hash__())
    r = len(find_common_elements(arr_2, arr_1))
    if r % 2 == 0:
        if m < n:
            print("YES")
        else:
            print("NO")
    else:
        if n >= m:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
