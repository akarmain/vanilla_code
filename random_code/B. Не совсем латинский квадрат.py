def main():
    for i in range(3):
        s_i = set(input())
        if "?" in s_i:
            print(*set("ABC")-s_i)

if __name__ == '__main__':
    for _ in range(int(input())):
        main()