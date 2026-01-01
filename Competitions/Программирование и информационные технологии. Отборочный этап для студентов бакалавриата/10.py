def main():
    n, k = map(int, input().split())
    s = input()

    m = len(s)
    MOD = 10**9 + 7
    pi = [0] * m
    for i in range(1, m):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    transitions = []

    for u in range(m):
        counts = {}
        for char_code in range(26):
            char = chr(ord("a") + char_code)
            v = u
            while v > 0 and char != s[v]:
                v = pi[v - 1]
            if char == s[v]:
                v += 1
            inc = 0
            if v == m:
                inc = 1
                v = pi[m - 1]

            key = (v, inc)
            counts[key] = counts.get(key, 0) + 1

        transitions.append(list(counts.items()))
    dp = [[0] * (k + 1) for _ in range(m)]
    dp[0][0] = 1
    for _ in range(n):
        new_dp = [[0] * (k + 1) for _ in range(m)]
        for u in range(m):
            for c in range(k + 1):
                val = dp[u][c]
                if val == 0:
                    continue
                for (next_state, inc), count_chars in transitions[u]:
                    next_c = c + inc
                    if next_c <= k:
                        ways = (val * count_chars) % MOD
                        new_dp[next_state][next_c] = (
                            new_dp[next_state][next_c] + ways
                        ) % MOD

        dp = new_dp

    ans = sum(dp[u][k] for u in range(m)) % MOD

    return str(ans)


if __name__ == "__main__":
    print(main())
