from math import ceil

def task_kompege_9541():
    odin = 19 # ((30 * 5) / 8)
    ans = ((odin * 262_144) / (2 ** 10))
    return ans



def task_kompege_9834():
    odin = ceil(60 / 8)
    ans = ((odin * 65_536) / (2 ** 10))
    return int(ans)



def task_kompege_4616():
    odin = ceil((13 * 294 ) / 8)
    ans = (131_072 * odin) / (2 ** 10)
    return ans


def task_kompege_9834():
    odin = ceil(60 / 8)
    ans = ((odin * 65_536) / (2 ** 10))
    return int(ans)



def task_kompege_5433():
    adres_bit = int((27 * 2**13) / 1316) - 19 - 48
    return int(adres_bit/5)


def task_kompege_4699():
    i = 11
    odin = ceil((250 * 11) / 8)
    return int((odin*65_536) / (2 ** 10))


def task_kompege_5183():
    i = 11
    l = 253
    odin = 510 # ceil((l * i) / 8)
    return (odin*65_536) / (2 ** 10)


def task_kompege_1855():
    i = 13
    l = 101

    odin = ceil((i * l) / 8)
    return (odin*2048) / (2 ** 10)


if __name__ == "__main__":
    # print("ANS task_kompege_9541:", task_kompege_9541())
    # print("ANS task_kompege_9834:", task_kompege_9834())
    # print("ANS task_kompege_4616:", task_kompege_4616())
    # print("ANS task_kompege_5433:", task_kompege_5433())
    # print("ANS task_kompege_4699:", task_kompege_4699())
    # print("ANS task_kompege_4699:", task_kompege_5183())
    print("ANS task_kompege_1855:", task_kompege_1855())
