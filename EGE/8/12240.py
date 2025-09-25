"""
Сколько существует девятеричных пятизначных чисел, содержащих в своей записи ровно одну цифру 5,
в которых никакие две одинаковые цифры не стоят рядом?
"""
from itertools import product

def main():
    ans = 0
    for d in product("012345678", repeat=5):
        if d[0] == "0":
            continue
        if d.count("5") == 1:
            if d[0] != d[1] and d[1] != d[2] and d[2] != d[3] and d[3] != d[4]:
                ans += 1
    return ans

if __name__ == "__main__":
    print("ANS:", main())
