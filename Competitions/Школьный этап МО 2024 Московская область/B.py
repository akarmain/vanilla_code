from itertools import permutations

def main():
    x, y = map(int, input().split())
    z = 5 - x - y
    elements = ['C'] * x + ['W'] * y + ['N'] * z
    unique_sequences = set(permutations(elements))
    point_values = [10, 20, 30, 40, 50]
    total_scores = set()

    for seq in unique_sequences:
        total = 0
        for i in range(5):
            if seq[i] == 'C':
                total += point_values[i]
            elif seq[i] == 'W':
                total -= point_values[i]
        total_scores.add(total)

    print(' '.join(map(str, sorted(total_scores))))

if __name__ == "__main__":
    while True:
        main()

