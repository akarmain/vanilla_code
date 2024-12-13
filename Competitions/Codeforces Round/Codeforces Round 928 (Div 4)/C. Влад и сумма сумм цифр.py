def main(pref_sum):
    n = int(input())
    print(pref_sum[n])


if __name__ == '__main__':
    pref_sum = [0] * 200001
    for i in range(1, 200001):
        pref_sum[i] = pref_sum[i - 1] + sum(list(map(int, str(i))))


    for _ in range(int(input())):
        main(pref_sum)
