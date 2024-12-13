def main():
    a = list(map(int, input()))
    b = list(map(int, input()))
    b = list(reversed(b))
    f = True

    # for i in range(len(a)):
    #     if a[i] == b[i]:
    #         f = False
    #
    # print(a)
    # print(b)

    return f


if __name__ == "__main__":
    for _ in range(int(input())):
        print("NO" if main() else "YES")
