import math

def min_moves(n, m, k):
    horizontal = m - 1
    vertical = n - 1

    common = min(horizontal, vertical)

    moves_diag = math.ceil(common / k)

    remaining = abs(horizontal - vertical)

    moves_remaining = math.ceil(remaining / k)

    return moves_diag + moves_remaining

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    result = min_moves(n, m, k)
    print(result)
