# https://education.yandex.ru/ege/task/6106ffcb-0b89-43be-bb9e-e8e706c5bbe2


def centroid(cluster):
    x_centr, y_centr = 0, 0
    minim = float('inf')
    for i, (x1, y1) in enumerate(cluster):
        res = sum(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 for x2, y2 in cluster)
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr


# Пример вызова функции
# x1, y1 = centroid(cluster)

def main():
    f = open("../../imputs/EGE_27_ya_0.txt")
    data_0 = []
    data_1 = []
    for i in f.readlines():
        x, y = map(float, i.replace(",", ".").split())
        if x < 0 and y<0:
            data_0.append((x, y))
        else:
            data_1.append((x, y))
    return abs(sum(centroid(data_0))/2*10000), abs(sum(centroid(data_1))/2*10000)


if __name__ == "__main__":
    print(main())
