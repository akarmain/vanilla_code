def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_sequence = 0
    current_sequence = 1

    for i in range(1, n):
        if a[i] == a[i - 1]:
            current_sequence += 1
        else:
            max_sequence = max(max_sequence, current_sequence)
            current_sequence = 
    max_sequence = max(max_sequence, current_sequence)
    min_burles = n - max_sequence

    return min_burles


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
