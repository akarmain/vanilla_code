"""
URL: https://education.yandex.ru/ege/task/10b197cd-2219-43da-aae1-d88f5ef74cc7
"""

from EGE.S27.utils import plot_clusters


def centroid(cluster: list[int, int]) -> (int, int):
    x_centr, y_centr = 0, 0
    minim = float('inf')
    for i, (x1, y1) in enumerate(cluster):
        res = sum(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 for x2, y2 in cluster)
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr


def main_A():
    with open("27A_1_20132.txt") as f:
        data_0 = []
        data_1 = []
        for line in f.readlines():
            x, y = map(float, line.replace(",", ".").split())
            if y > 3:
                data_0.append([x, y])
            else:
                data_1.append([x, y])


if __name__ == "__main__":
    print(*main())
