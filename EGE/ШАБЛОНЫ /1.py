from itertools import permutations


def main():
    # По строчно перечисляем связи каждого пункта
    tab = '57 457 46 236 12 348 128 67'.split()

    # все пары связей на изображении
    pic = 'cg cf gh gd hd db eb ae af fb'.split()

    print(*range(1, 9))
    for var in permutations('abcdefgh'):
        var = ''.join(var)
        if all(str(var.index(x) + 1) in tab[var.index(y)] for x, y in pic):
            print(*var)


if __name__ == "__main__":
    print("ANS:", main())
