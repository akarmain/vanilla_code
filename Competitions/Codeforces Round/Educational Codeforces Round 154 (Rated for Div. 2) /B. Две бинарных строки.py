def main():
    a = list(input())
    b = list(reversed(list(input())))
    print(a)
    print(b)
    return


if __name__ == "__main__":
    for _ in range(int(input())):
        print("YES" if main() else "NO")
