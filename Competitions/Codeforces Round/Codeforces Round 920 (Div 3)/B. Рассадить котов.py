def min_operations_to_arrange_cats(t, test_cases):
    results = []
    for n, s, f in test_cases:
        s = [int(char) for char in s]
        f = [int(char) for char in f]
        operations = 0
        for i in range(n):
            if s[i] != f[i]:
                operations += 1
        direct_moves = min(s.count(1), f.count(1)) - sum([s[i] and f[i] for i in range(n)])
        operations -= direct_moves
        results.append(operations)
    return results



if __name__ == '__main__':
    t = int(input())
    test_cases = []
    for _ in range(t):
        n = int(input())
        s = input()
        f = input()
        test_cases.append((n, s, f))
    for ans in  min_operations_to_arrange_cats(t, test_cases):
        print(ans)
