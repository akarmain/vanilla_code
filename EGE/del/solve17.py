from pathlib import Path

def solve(path: str = "17.txt") -> tuple[int, int]:
    nums = [int(x) for x in Path(path).read_text().split()]
    max70 = max(n for n in nums if abs(n) % 100 == 70)  # <-- фикс

    count = 0
    max_sum = -10**18
    for i in range(len(nums) - 2):
        a, b, c = nums[i], nums[i + 1], nums[i + 2]
        if a >= 0 and b >= 0 and c >= 0:
            s = a + b + c
            if s <= max70:
                count += 1
                max_sum = max(max_sum, s)
    return count, max_sum

print(*solve("17.txt"))
