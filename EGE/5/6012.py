"""
№ 6012 ФИПИ 03.02.23 (Уровень: Базовый)
"""


def algos(n):
    bn = bin(n)[2:]
    if bn.count("1") % 2 == 0:
        return int("1" + (bn + "0")[2:], 2)
    return int(f"11{bn[2:]}1", 2)


def main():
    # От дрочить это говно до 10.05.25
    nx = min(algos(n) for n in range(1, 1000) if algos(n) > 49)
    return min(n for n in range(1, 1000) if algos(n) == nx)


if __name__ == "__main__":
    print("ANS:", main())
