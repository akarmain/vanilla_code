def main():
	x, n = map(int, input().split())
	if n % 2 != 0:
		return x
	return 0


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
