def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    # dp[i][j] — минимальная сумма для первых i элементов, разделенных на j частей
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Начинаем с пустого массива и 0 частей

    # Перебираем возможные разделы
    for j in range(1, k + 1):
        for i in range(1, n + 1):
            for m in range(i):
                dp[i][j] = min(dp[i][j], max(dp[m][j - 1], prefix[i] - prefix[m]))

    result = 0
    for i in range(k, n + 1):
        result = max(result, dp[i][k])

    return result


if __name__ == '__main__':
    print(main())
