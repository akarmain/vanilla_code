"""
URL: https://education.yandex.ru/ege/task/04b011f5-651b-4d46-a858-dc0d0995990c

"""


def ff(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1-x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def is_social(animal, animals):
    count = sum(1 for other in animals if ff(animal, other) <= 0.1) - 1  # Минус 1, т.к. точка совпадает с собой
    return count >= 14

def anal(cl: list):
    ans = list()
    dic = dict()
    lll = []
    c = 0
    for cell, animals in grid.items():
        social_count = sum(is_social(animal, animals) for animal in animals)
        grid_counts[cell] = (social_count, len(animals) - social_count)

    for i in range(len(cl)):
        for p1 in cl:

            if ff(cl[i], p1) > 0.1:
                lll.append(ff(cl[i], p1))
                try:
                    dic[i] += 1
                except:
                    dic[i] = 1
    lll.sort()
    print(dic)
        # if c > 14:
        #     ans.append(c)
    # if c >= 14:
    #     ans += 1

    return ans


def main_a():
    with open("../../imputs/EGE_27_ya_4_A.txt") as f:
        data_4 = []
        data_5 = []
        for line in f.readlines():
            x, y = map(float, line.replace(",", ".").split())
            if (1 < x < 2) and (1 < y < 2):
                data_4.append([x, y])
            elif (2 < x < 3) and (1 < y < 2):
                data_5.append([x, y])
    print(len(data_4))
    print(anal(data_4))

    # if y < 4 and x < 4:
    #     data_0.append([x, y])
    # elif x > 4 and y < 7:
    #     data_1.append([x, y])
    ...


def main_b():
    ...


if __name__ == "__main__":
    d = {}
    d[1] = 1
    d[2] = 2
    print(d)
    print("ANS_A:", main_a())
    print("ANS_A:", main_b())
