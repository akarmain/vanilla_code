"""
URL: https://education.yandex.ru/ege/task/10b197cd-2219-43da-aae1-d88f5ef74cc7
"""


def centroid(cluster: list[int, int]) -> (int, int):
    x_centr, y_centr = 0, 0
    minim = float('inf')
    for i, (x1, y1) in enumerate(cluster):
        res = sum(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 for x2, y2 in cluster)
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr


def main_А():
    data_1 = []
    data_2 = []
    for line in open("../../imputs/EGE_27_A_ya_пробник_0.txt"):
        x, y = map(float, line.split())
        if y > 3:
            data_2.append([x, y])
        else:
            data_1.append([x, y])
    p1, p2 = centroid(data_1), centroid(data_2)
    Px = ((p1[0] + p2[0]) / 2) * 10000
    Py = ((p1[1] + p2[1]) / 2) * 10000
    return int(Px), int(Py)


def main_B():
    data_1 = []
    data_2 = []
    data_3 = []
    for line in open("../../imputs/EGE_27_B_ya_пробник_0.txt"):
        x, y = map(float, line.replace(",", ".").split())
        if x < 4 and y < 4:
            data_1.append([x, y])
        elif y > 3 and y < 7:
            data_2.append([x, y])
        else:
            data_3.append([x, y])
    p1, p2, p3 = centroid(data_1), centroid(data_2), centroid(data_3)
    Px = ((p1[0] + p2[0] + p3[0]) / 3) * 10000
    Py = ((p1[1] + p2[1] + p3[1]) / 3) * 10000
    return int(Px), int(Py)


if __name__ == "__main__":
    print("ANS:", *main_А())
    print("ANS:", main_B())
