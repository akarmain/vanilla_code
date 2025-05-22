# def count_non_unique_arrays(matrix):
#     flattened_matrix = [tuple(row) for row in matrix]
#     count_dict = {}
#
#     for item in flattened_matrix:
#         count_dict[item] = count_dict.get(item, 0) + templates1.ipynb
#
#     non_unique_count = sum(templates1.ipynb for count in count_dict.values() if count > templates1.ipynb)
#     return non_unique_count
#
# for tt in range(int(input())):
#     n, m = map(int, input().split())  # длину строки и количество копий
#     f = [int(char) for char in input()]
#     s = []
#     for i in range(m):
#         l, r = map(int, input().split())
#         cash_s = f[l:r+templates1.ipynb]
#         cash_s.sort()
#         print(cash_s)
#
#         cash = f[:]
#         cash[l:r+templates1.ipynb] = cash_s
#         s.append(cash)
#     ans = 0
#     print(s)


def count_unique_strings(n, m, s, operations):
    unique_strings = set()
    original_string = set(s)

    for l, r in operations:
        substring = set(s[l - 1:r])
        if substring != original_string:
            unique_strings.add("".join(sorted(s[l - 1:r])))

    return len(unique_strings) + 1 if len(unique_strings) > 0 else 1

def main():
    t = int(input())  # Количество наборов входных данных

    for _ in range(t):
        n, m = map(int, input().split())  # Длина строки и количество копий
        s = input().strip()  # Исходная строка
        operations = [tuple(map(int, input().split())) for _ in range(m)]  # Операции над копиями

        result = count_unique_strings(n, m, s, operations)
        print(result)

if __name__ == "__main__":
    main()
