def algos(n):
    bn = bin(n)[2:].zfill(8)
    n_bn = ''
    for b in bn:
        if b == '0':
            n_bn += "1"
        else:
            n_bn += "0"
    # n_bn = n_bn
    return int(n_bn, 2) + 1


def main():
    for i in range(1, 128):
        if algos(i) == 221:
            print(i, algos(i))


if __name__ == "__main__":
    print(algos(1))
    print("ANS:", main())
