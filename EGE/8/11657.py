"""
Сколько существует восьмеричных шестизначных чисел, не содержащих в своей записи цифру 3,
 в которых все цифры различны и хотя бы две чётные стоят рядом?
"""
from itertools import permutations

def main():
    ans = 0
    for d in permutations("0124567", r=6): # зарзу без 3
        if d[0] == "0":
            continue

        # 3) Проверяем, есть ли хотя бы одна пара соседних чётных:
        #    чётными в восьмеричной считаем {0,2,4,6}.
        #    Пробежимся по i=0..4 и посмотрим, есть ли d[i] и d[i+1] одновременно чётные.
        found_two_even = False
        for i in range(5):
            # int(d[i], 8) превращает символ '0'..'7' → в число 0..7,
            # %2 == 0 означает «чётная».
            if (int(d[i], 8) % 2 == 0) and (int(d[i+1], 8) % 2 == 0):
                found_two_even = True
                break

        if not found_two_even:
            continue

        ans += 1

    return ans


if __name__ == "__main__":
    print("ANS:", main())
