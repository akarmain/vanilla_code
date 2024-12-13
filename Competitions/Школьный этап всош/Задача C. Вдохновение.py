def main():
    days = int(input())
    a_and_b = int(input())
    a = int(input())
    b = int(input())
    ans = days - a - b + a_and_b
    if a_and_b > a or a_and_b > b:
        return -1
    if ans < 0:
        return -1
    return ans


if __name__ == '__main__':
    print(main())
