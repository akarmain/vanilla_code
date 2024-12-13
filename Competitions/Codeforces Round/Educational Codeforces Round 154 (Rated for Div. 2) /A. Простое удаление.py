def main():
    arr = input()
    # if not ((3 in arr) or (7 in arr) or (9 in arr) or (1 in arr)):
    return "17" if arr.find("7") > arr.find("1") else 71


if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
