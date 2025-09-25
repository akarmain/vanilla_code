"""
URL: https://kompege.ru/task

№ 9692 Danov2307 (Уровень: Средний)
"""


def algos(n):
    bn = bin(n)[2:]
    if n % 2 == 0:
        return int(f"{bin(bn.count("1"))[2:]}{bn}{bn.count('1') % 2}", 2)
    return int(f"{bn}0{bin(bn.count("1"))[2:]}", 2)


def main():
    mx = max(algos(n) for n in range(1, 1000) if algos(n) < 256)
    return min(n for n in range(1, 1000) if algos(n) == mx)


if __name__ == "__main__":
    print("ANS:", main())
