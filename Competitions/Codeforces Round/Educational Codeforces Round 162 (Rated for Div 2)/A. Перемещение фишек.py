def main():
    n = int(input())
    arr = map(int, input().split())
    arr_str = ''.join(map(str, arr))
    print(arr_str[arr_str.find('1'): arr_str.rfind("1")].count("0"))


if __name__ == '__main__':
    for _ in range(int(input())): main()
