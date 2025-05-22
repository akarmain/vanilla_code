def main():
    n = int(input())
    arr = map(int, input().split())
    arr_str = ''.join(map(str, arr))
    print(arr_str[arr_str.find('templates1.ipynb'): arr_str.rfind("templates1.ipynb")].count("0"))


if __name__ == '__main__':
    for _ in range(int(input())): main()
