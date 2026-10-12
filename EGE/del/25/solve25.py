"""
Solution for task №25 (cluster rectangles) using pure Python.
Reads files 25_A.txt and 25_B.txt located in the same folder.

Algorithm:
- k-means (many random seeds) to split into the required number of clusters;
- validate each cluster by minimal bounding rectangle (rotating calipers) that must fit H×W;
- choose the valid partition with minimal inertia;
- cluster center = medoid (point with minimal sum of distances).
"""

from __future__ import annotations

import math
import random
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

Point = Tuple[float, float]


# ---------------- I/O ---------------- #
def read_points(path: Path) -> List[Point]:
    pts: List[Point] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = line.replace(",", ".").split()
        pts.append((float(a), float(b)))
    return pts


# ------------- Geometry ------------- #
def dist(a: Point, b: Point) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def cross(o: Point, a: Point, b: Point) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points: Sequence[Point]) -> List[Point]:
    pts = sorted(points)
    if len(pts) <= 1:
        return list(pts)

    lower: List[Point] = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper: List[Point] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def min_bounding_box(pts: Sequence[Point]) -> Tuple[float, float]:
    """Return (width, height) of minimal-area bounding rectangle (free rotation)."""
    if len(pts) == 1:
        return 0.0, 0.0

    hull = convex_hull(pts)
    if len(hull) == 2:
        d = dist(hull[0], hull[1])
        return d, 0.0

    best_area = float("inf")
    best_wh = (0.0, 0.0)

    for i in range(len(hull)):
        p1 = hull[i]
        p2 = hull[(i + 1) % len(hull)]
        angle = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
        cos_a, sin_a = math.cos(-angle), math.sin(-angle)

        xs: List[float] = []
        ys: List[float] = []
        for x, y in hull:
            xr = x * cos_a - y * sin_a
            yr = x * sin_a + y * cos_a
            xs.append(xr)
            ys.append(yr)

        width = max(xs) - min(xs)
        height = max(ys) - min(ys)
        area = width * height
        if area < best_area:
            best_area = area
            best_wh = (width, height)

    return best_wh


def bbox_fits(pts: Sequence[Point], H: float, W: float) -> bool:
    w, h = min_bounding_box(pts)
    return (w <= W + 1e-9 and h <= H + 1e-9) or (w <= H + 1e-9 and h <= W + 1e-9)


# ------------- Clustering ------------- #
def kmeans(points: Sequence[Point], k: int, iters: int = 40) -> Tuple[List[Point], List[List[Point]]]:
    centers = random.sample(points, k)
    for _ in range(iters):
        clusters: List[List[Point]] = [[] for _ in range(k)]
        for p in points:
            idx = min(range(k), key=lambda i: (p[0] - centers[i][0]) ** 2 + (p[1] - centers[i][1]) ** 2)
            clusters[idx].append(p)

        new_centers: List[Point] = []
        for c in clusters:
            if not c:
                new_centers.append(random.choice(points))
            else:
                cx = sum(p[0] for p in c) / len(c)
                cy = sum(p[1] for p in c) / len(c)
                new_centers.append((cx, cy))

        shift = max(dist(centers[i], new_centers[i]) for i in range(k))
        centers = new_centers
        if shift < 1e-7:
            break
    return centers, clusters


def find_partition(points: Sequence[Point], k: int, H: float, W: float, seeds: int = 200) -> List[List[Point]]:
    """
    Run multiple k-means seeds; keep valid partition with minimal inertia.
    Deterministic: iterates seeds in order and resets RNG each time.
    """
    best_clusters: List[List[Point]] | None = None
    best_inertia = float("inf")

    for seed in range(seeds):
        random.seed(seed)
        centers, clusters = kmeans(points, k, iters=30)
        if any(len(c) == 0 for c in clusters):
            continue
        if not all(bbox_fits(c, H, W) for c in clusters):
            continue

        inertia = sum(
            (p[0] - centers[i][0]) ** 2 + (p[1] - centers[i][1]) ** 2
            for i, c in enumerate(clusters)
            for p in c
        )
        if inertia < best_inertia:
            best_inertia = inertia
            best_clusters = clusters
        # tie-breaker: prefer partition with lexicographically smaller sorted sizes
        elif inertia == best_inertia and best_clusters is not None:
            if sorted(len(c) for c in clusters) < sorted(len(c) for c in best_clusters):
                best_clusters = clusters

    if best_clusters is None:
        raise RuntimeError("Valid clusterization not found; increase seeds.")
    return best_clusters


def medoid(cluster: Sequence[Point]) -> Point:
    """Cluster center by task definition: point minimizing sum of distances (unique)."""
    best_p = cluster[0]
    best_sum = float("inf")
    for p in cluster:
        s = 0.0
        for q in cluster:
            s += dist(p, q)
        if s < best_sum:
            best_sum = s
            best_p = p
    return best_p


# ------------- Task parts ------------- #
def solve_A(path: Path) -> Tuple[int, int]:
    points = read_points(path)
    clusters = find_partition(points, k=2, H=5, W=7, seeds=50)

    medoids = [medoid(c) for c in clusters]
    sizes = [len(c) for c in clusters]
    idx_max = max(range(2), key=lambda i: sizes[i])
    idx_min = min(range(2), key=lambda i: sizes[i])

    center_max = medoids[idx_max]
    center_min = medoids[idx_min]

    P1 = sum(1 for p in points if dist(p, center_max) <= 0.7 + 1e-9)
    P2 = sum(1 for p in points if dist(p, center_min) >= 1.3 - 1e-9)
    return P1, P2


def solve_B(path: Path) -> Tuple[int, int]:
    points = read_points(path)
    clusters = find_partition(points, k=3, H=5, W=5, seeds=80)
    centers = [medoid(c) for c in clusters]

    target: Point = (1.7, 2.3)
    dists = [dist(c, target) for c in centers]
    Q1 = min(dists)
    Q2 = max(dists)
    return int(Q1 * 10000), int(Q2 * 10000)


# ------------- Main ------------- #
def main() -> None:
    base = Path(__file__).resolve().parent
    P1, P2 = solve_A(base / "25_A.txt")
    Q1, Q2 = solve_B(base / "25_B.txt")

    print(f"{P1} {P2}")
    print(f"{Q1} {Q2}")


if __name__ == "__main__":
    main()
