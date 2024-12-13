def main():
    x, y, z = map(int, input().split())
    print(x^y^z)

if __name__ == '__main__':
    for _ in range(int(input())):
        main()