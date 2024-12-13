def check_carpet(n, k, carpet):
    for col1 in range(k):
        for col2 in range(col1 + 1, k):
            for col3 in range(col2 + 1, k):
                for col4 in range(col3 + 1, k):
                    column1 = [carpet[i][col1] for i in range(n)]
                    column2 = [carpet[i][col2] for i in range(n)]
                    column3 = [carpet[i][col3] for i in range(n)]
                    column4 = [carpet[i][col4] for i in range(n)]

                    if "v" in column1 and "i" in column2 and "k" in column3 and "a" in column4:
                        return "YES"
    return "NO"


def main():
    global n, k
    n, k = map(int, input().split())
    cover = []
    for i in range(n):
        cover.append(list(input()))

    return check_carpet(n, k, cover)


if __name__ == "__main__":
    for i in range(int(input())):
        result = main()
        print(result)
