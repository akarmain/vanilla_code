from functools import lru_cache

TARGET = 52
FORBIDDEN = {31, 45}
REQUIRED = {16, 24}


def next_values(x: int):
    for nx in (x + 2, x + 3, x * 2):
        if nx <= TARGET:
            yield nx


@lru_cache(maxsize=None)
def count_paths(x: int, seen16: bool, seen24: bool) -> int:
    if x in FORBIDDEN:
        return 0

    seen16 = seen16 or (x == 16)
    seen24 = seen24 or (x == 24)

    if x == TARGET:
        return int(seen16 or seen24)

    return sum(count_paths(nx, seen16, seen24) for nx in next_values(x))


def main():
    print(count_paths(10, False, False))


if __name__ == "__main__":
    main()
