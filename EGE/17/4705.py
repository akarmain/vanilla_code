def main():
    data = []
    max_3 = 0
    max_sum = 0
    count_pars = 0
    for d in open("../../imputs/EGE_4705.txt").readlines():
        d = int(d)
        data.append(d)
        if str(d)[-1] == "3":
            max_3 = max(max_3, d)

    for i in range(len(data) - 1):
        x1 = data[i]
        x2 = data[i + 1]
        c_x1 = str(x1)[-1] == "3"
        c_x2 = str(x2)[-1] == "3"
        if c_x1 + c_x2 == 1:
            if x1 ** 2 + x2 ** 2 >= max_3 ** 2:
                max_sum = max(max_sum, x1 ** 2 + x2 ** 2)
                count_pars += 1
    return count_pars, max_sum


if __name__ == "__main__":
    print("ANS:", *main())
