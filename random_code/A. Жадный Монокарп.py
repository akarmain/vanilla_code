def main():
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    arr.sort(reverse=True)  # Сортируем массив в порядке убывания
    s = 0  # Текущая сумма
    for x in arr:
        if s + x <= k:  # Если можем добавить элемент в сумму
            s += x
        else:
            break  # Иначе прекращаем
    return k - s

if __name__ == '__main__':
    for i in range(int(input())):
        print(main())

"""
2
5 4
4 templates1.ipynb 2 3 2
5 10
4 templates1.ipynb 2 3 2"""
