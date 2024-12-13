def find_square_area(corners):
    corners.sort()
    side = max(abs(corners[0][0] - corners[1][0]), abs(corners[2][1] - corners[3][1]))
    return side ** 2


def main():
    corners = []
    for _ in range(4):
        x, y = map(int, input().split())
        corners.append((x, y))
    area = find_square_area(corners)
    print(area)


if __name__ == "__main__":
    for _ in range(int(input())):
        main()
