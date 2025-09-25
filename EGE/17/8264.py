def main():
    data = []
    all_min = 9999
    count_pars = 0
    max_sum_map = 0
    for l in open("../../imputs/EGE_8264.txt"):
        d = int(l)
        data.append(d)
        all_min = min(abs(d), all_min)

    for i in range(len(data) - 1):
        x1 = data[i]
        x2 = data[i + 1]
        if x1 > 0 and x2 <= 0 or x2 > 0 and x1 <= 0:
            if x1 + x2 > 0 and (x1 + x2) % all_min == 0:
                max_sum_map = max(max_sum_map, x1 + x2)
                count_pars += 1
    return count_pars, max_sum_map


if __name__ == "__main__":
    print("ANS:", *main())
