"""
Visualization for task 25 without external graphics libraries.
Creates an SVG (plot.svg) in this folder, showing clusters, medoids,
and minimal bounding rectangles for files 25_A.txt and 25_B.txt.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import List, Sequence, Tuple

base = Path(__file__).resolve().parent
sys.path.append(str(base))
from solve25 import (  # type: ignore
    Point,
    bbox_fits,
    find_partition,
    medoid,
    read_points,
)


# ---------- Geometry helpers (copy for rectangle corners) ---------- #
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


def min_bounding_rect(points: Sequence[Point]) -> List[Point]:
    """Return corners (4 points) of minimal-area bounding rectangle."""
    hull = convex_hull(points)
    if len(hull) == 1:
        p = hull[0]
        return [p, p, p, p]
    if len(hull) == 2:
        p1, p2 = hull
        return [p1, p2, p2, p1]

    best_area = float("inf")
    best_rect = None

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
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        width = maxx - minx
        height = maxy - miny
        area = width * height
        if area < best_area:
            rect_local = [
                (minx, miny),
                (maxx, miny),
                (maxx, maxy),
                (minx, maxy),
            ]
            cos_b, sin_b = math.cos(angle), math.sin(angle)
            rect_global = [
                (xl * cos_b - yl * sin_b, xl * sin_b + yl * cos_b) for xl, yl in rect_local
            ]
            best_area = area
            best_rect = rect_global
    return best_rect  # type: ignore


# ---------- SVG renderer ---------- #
def to_svg_points(points: Sequence[Point], bbox, width: int, height: int):
    (minx, miny, maxx, maxy) = bbox
    sx = (width - 40) / (maxx - minx) if maxx != minx else 1.0
    sy = (height - 40) / (maxy - miny) if maxy != miny else 1.0
    scale = min(sx, sy)
    tx = 20 - minx * scale
    ty = 20 - miny * scale

    def conv(p: Point) -> Point:
        return (p[0] * scale + tx, height - (p[1] * scale + ty))

    return [conv(p) for p in points], conv


def render_case(svg_parts: List[str], origin_x: int, title: str, points: Sequence[Point], clusters: Sequence[Sequence[Point]], H: float, W: float):
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
    all_pts = points
    minx = min(p[0] for p in all_pts)
    maxx = max(p[0] for p in all_pts)
    miny = min(p[1] for p in all_pts)
    maxy = max(p[1] for p in all_pts)
    bbox = (minx, miny, maxx, maxy)
    width = 500
    height = 500
    _, conv = to_svg_points(all_pts, bbox, width, height)

    svg_parts.append(f'<g transform="translate({origin_x},20)">')
    svg_parts.append(f'<text x="{width/2}" y="15" text-anchor="middle" font-size="14">{title}</text>')

    # grid
    svg_parts.append('<rect x="0" y="0" width="{0}" height="{1}" fill="none" stroke="#ccc" stroke-width="1"/>'.format(width, height))

    for idx, cluster in enumerate(clusters):
        col = colors[idx % len(colors)]
        pts_svg = [conv(p) for p in cluster]
        svg_parts.extend(
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2" fill="{col}" fill-opacity="0.6"/>' for x, y in pts_svg
        )
        m = medoid(cluster)
        mx, my = conv(m)
        svg_parts.append(f'<polygon points="{mx-6:.2f},{my} {mx:.2f},{my-8:.2f} {mx+6:.2f},{my} {mx:.2f},{my+8:.2f}" fill="black"/>')
        svg_parts.append(f'<text x="{mx+6:.2f}" y="{my-6:.2f}" font-size="10" fill="black">M{idx+1}</text>')

        rect = min_bounding_rect(cluster)
        rect_pts = [conv(p) for p in rect] + [conv(rect[0])]
        path_d = " ".join(f"L {x:.2f} {y:.2f}" for x, y in rect_pts[1:])
        svg_parts.append(f'<path d="M {rect_pts[0][0]:.2f} {rect_pts[0][1]:.2f} {path_d}" stroke="{col}" stroke-width="1.2" fill="none"/>')

        fits = bbox_fits(cluster, H, W)
        svg_parts.append(f'<text x="{mx+6:.2f}" y="{my+10:.2f}" font-size="9" fill="{col}">fits {H}x{W}: {"yes" if fits else "no"}</text>')

    svg_parts.append("</g>")


def main():
    pts_a = read_points(base / "25_A.txt")
    clusters_a = find_partition(pts_a, k=2, H=5, W=7, seeds=60)

    pts_b = read_points(base / "25_B.txt")
    clusters_b = find_partition(pts_b, k=3, H=5, W=5, seeds=100)

    svg_parts: List[str] = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1020" height="540">',
        '<rect width="100%" height="100%" fill="white"/>',
    ]
    render_case(svg_parts, origin_x=10, title="File A (H=5, W=7)", points=pts_a, clusters=clusters_a, H=5, W=7)
    render_case(svg_parts, origin_x=520, title="File B (H=5, W=5)", points=pts_b, clusters=clusters_b, H=5, W=5)
    svg_parts.append("</svg>")

    out_path = base / "plot.svg"
    out_path.write_text("\n".join(svg_parts), encoding="utf-8")
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
