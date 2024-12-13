def main():
    a, b, c = map(int, input().split())
    if c % 2 == 0:
        if a <= b:
            print("Second")
        else:
            print("First")
    else:
        if a + c < b + c:
            print("Second")
        else:
            print("First")


if __name__ == "__main__":
    for i in range(int(input())):
        main()
"""
First
First
Second
First
Second
"""
