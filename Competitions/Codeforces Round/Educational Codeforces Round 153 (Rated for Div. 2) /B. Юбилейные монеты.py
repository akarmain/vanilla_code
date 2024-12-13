def main():
    m, k, a_one, a_k = map(int, input().split())
    ans = 0
    m -= m//k*a_k
    print(ans, m)


# денег больше нет нужно использовать юбелярные монеты


if __name__ == "__main__":
    for _ in range(int(input())):
        main()
