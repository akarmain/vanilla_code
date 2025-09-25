
def centroid(cluster: list[int, int]) -> (int, int):
    x_centr, y_centr = 0, 0
    minim = float('inf')
    for i, (x1, y1) in enumerate(cluster):
        res = sum(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 for x2, y2 in cluster)
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr


def main():
    with open("EGE_27_ya_3_B.txt") as f:
        data_0 = []
        data_1 = []
        for line in f.readlines():
            x, y = map(float, line.replace(",", ".").split())
            if y > 3:
                data_0.append([x, y])
            else:
                data_1.append([x, y])

    c_0 = centroid(data_0)
    c_1 = centroid(data_1)
    Px = ((c_0[0] + c_1[0]) / 2) * 10000
    Py = ((c_0[1] + c_1[1]) / 2) * 10000

    return int(Px), int(Py)




if __name__ == "__main__":
    print(*main())
