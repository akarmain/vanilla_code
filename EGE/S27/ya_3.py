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
    with open("../../imputs/EGE_27_ya_3_B.txt") as f:
        data_0 = []
        data_1 = []
        for line in f.readlines():
            x, y = map(float, line.replace(",", ".").split())
            if y > 3:
                data_0.append([x, y])
            else:
                data_1.append([x, y])
    #
    # plot_clusters(data_0)
    # plot_clusters(data_1)
    c_0 = centroid(data_0)
    c_1 = centroid(data_1)

    Px = ((c_0[0] + c_1[0]) / 2) * 10000
    Py = ((c_0[1] + c_1[1]) / 2) * 10000

    return int(Px), int(Py)


def main():
    with open("../../imputs/EGE_27_ya_3_B.txt") as f:
        data_0 = []
        data_1 = []
        data_2 = []
        main_c = []
        for line in f.readlines():
            x, y = map(float, line.replace(",", ".").split())
            main_c.append([x, y])
            if y < 4 and x < 4:
                data_0.append([x, y])
            elif x > 4 and y < 7:
                data_1.append([x, y])
            else:
                data_2.append([x, y])
    print(len(data_0) + len(data_1) + len(data_2))
    plot_clusters(data_0, data_1, data_2)
    c_0 = centroid(data_0)
    c_1 = centroid(data_1)
    c_2 = centroid(data_2)

    Px = ((c_0[0] + c_1[0] + c_2[0]) / 3) * 10000
    Py = ((c_0[1] + c_1[1] + c_2[1]) / 3) * 10000

    return int(Px), int(Py)


if __name__ == "__main__":
    print(*main())
    print(37522, 51277)
