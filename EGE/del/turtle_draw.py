"""
Approximate drawing of the turtle path from the task, with labeled edges.

If GUI (tkinter) is unavailable (e.g., headless environment), the script will
skip drawing and just print the perimeter.
"""

import math
import os


def build_segments():
    """Return list of segments as (x1, y1, x2, y2, length)."""
    x = y = 0.0
    angle = 90.0  # facing +Y
    segs = []

    def fwd(d: float):
        nonlocal x, y
        rad = math.radians(angle)
        nx = x + d * math.cos(rad)
        ny = y + d * math.sin(rad)
        segs.append((x, y, nx, ny, d))
        x, y = nx, ny

    def right(deg: float):
        nonlocal angle
        angle -= deg

    # Повтори 2 [Повтори 2 [Вперёд 180 Направо 120] Направо 120]
    for _ in range(2):
        for _ in range(2):
            fwd(180)
            right(120)
        right(120)

    right(150)
    fwd(15)
    right(90)
    fwd(360)
    right(90)
    fwd(15)
    right(30)
    fwd(74)

    return segs


def draw(segs):
    """Draw segments with labels using turtle. Requires GUI environment."""
    import turtle

    WIDTH, HEIGHT = 900, 700
    turtle.setup(WIDTH, HEIGHT)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    label = turtle.Turtle()
    label.hideturtle()
    label.speed(0)
    label.penup()

    xs = [x for s in segs for x in s[:4:2]]
    ys = [y for s in segs for y in s[1:4:2]]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    cx, cy = (minx + maxx) / 2, (miny + maxy) / 2
    scale = min(
        (WIDTH - 120) / (maxx - minx if maxx != minx else 1),
        (HEIGHT - 120) / (maxy - miny if maxy != miny else 1),
    )

    def to_screen(x, y):
        return (x - cx) * scale, (y - cy) * scale

    t.penup()
    x0, y0 = to_screen(segs[0][0], segs[0][1])
    t.goto(x0, y0)
    t.pendown()

    for idx, (x1, y1, x2, y2, length) in enumerate(segs):
        sx1, sy1 = to_screen(x1, y1)
        sx2, sy2 = to_screen(x2, y2)
        t.goto(sx2, sy2)

        mx, my = (sx1 + sx2) / 2, (sy1 + sy2) / 2
        label.goto(mx, my)
        label.write(f"{idx + 1}: {int(length)}", align="center", font=("Arial", 10, "normal"))

    turtle.done()


def main():
    segs = build_segments()
    perimeter = sum(length for *_, length in segs)
    print(perimeter)

    # Try to draw if a display is available
    has_display = bool(os.environ.get("DISPLAY")) or os.name == "nt"
    if has_display:
        try:
            draw(segs)
        except Exception as e:  # noqa: BLE001
            print(f"Drawing skipped: {e}")
    else:
        print("GUI not available; drawing skipped.")


if __name__ == "__main__":
    main()
