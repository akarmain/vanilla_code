from functools import lru_cache

def count_programs(x: int, seen32: bool, seen35: bool) -> int:
    e = 44
    # Превысили конечное число — таких программ нет
    if x > e:
        return 0
    # Перед продвижением дальше отмечаем, встретились ли уже 32 или 35
    seen32 |= (x == 32)
    seen35 |= (x == 35)
    # Достигли конца — считаем путь только если оба числа были в траектории
    if x == e:
        return 1 if (seen32 and seen35) else 0
    # Пробуем все три команды
    return (
        count_programs(x + 3, seen32, seen35) +
        count_programs(x + 4, seen32, seen35) +
        count_programs(x + 2, seen32, seen35)
    )

def main():
    return count_programs(6, False, False)

if __name__ == "__main__":
    print("Ответ:", main())
