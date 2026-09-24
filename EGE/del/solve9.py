from collections import Counter
from pathlib import Path

def solve(path: str = "9.txt") -> int:
    rows = [list(map(int, line.split())) for line in Path(path).read_text().strip().splitlines()]
    last_row_min_repeat = None

    for row in rows:
        freq = Counter(row)
        # Exactly one number appears 3 times, one number 2 times, the rest once: counts are [3,2,1,1]
        if sorted(freq.values(), reverse=True) != [3, 2, 1, 1]:
            continue

        non_repeat_sum = sum(num for num, cnt in freq.items() if cnt == 1)
        repeat_nums = [num for num, cnt in freq.items() if cnt > 1]

        if non_repeat_sum <= min(repeat_nums):
            last_row_min_repeat = min(repeat_nums)  # overwrite to keep the row with the largest index

    if last_row_min_repeat is None:
        raise ValueError("No rows satisfy the conditions")

    return abs(last_row_min_repeat)

def main():
    print(solve())

if __name__ == "__main__":
    main()
