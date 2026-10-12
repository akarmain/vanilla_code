from __future__ import annotations

import heapq
import sys
from pathlib import Path
from typing import List, Tuple


def solve(path: str | Path, limit: int = 900) -> Tuple[int, int]:
    data = Path(path).read_text().split()
    it = iter(data)

    n = int(next(it))
    k = int(next(it))

    # свободные ячейки: (cost, idx)
    free: List[Tuple[int, int]] = [(int(next(it)), idx) for idx in range(1, n + 1)]
    heapq.heapify(free)

    # занятые ячейки: (end_time, cost, idx)
    busy: List[Tuple[int, int, int]] = []

    requests = [(int(next(it)), int(next(it))) for _ in range(k)]
    requests.sort()

    total_cost = 0
    last_cell = 0

    for t, s in requests:
        # освободить все ячейки к моменту t (включая равные)
        while busy and busy[0][0] <= t:
            end_time, cost, idx = heapq.heappop(busy)
            heapq.heappush(free, (cost, idx))

        if not free:
            continue  # пассажир уходит

        cost, idx = heapq.heappop(free)
        heapq.heappush(busy, (t + s, cost, idx))

        if t <= limit:  # изменить на t < limit при другой трактовке
            total_cost += cost
            last_cell = idx

    return total_cost, last_cell


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python 24.py <input_file>")
        raise SystemExit(2)

    total, cell = solve(sys.argv[1])
    print(total, cell)


if __name__ == "__main__":
    main()
