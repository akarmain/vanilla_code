def can_pass(segments, k):
    # Начальная позиция игрока
    position = 0

    for l, r in segments:
        # Если текущий отрезок слишком далеко, игрок не может достичь его
        if l > position + k:
            return False
        # Обновляем позицию игрока, убедившись, что она в пределах текущего отрезка
        position = max(position, l)
        position = min(position + k, r)

    return True

def binary_search(segments):
    # Начальные и конечные границы для k
    left, right = 0, max(r for _, r in segments)

    while left < right:
        mid = (left + right) // 2
        if can_pass(segments, mid):
            right = mid
        else:
            left = mid + 1

    return left

# Чтение входных данных и вывод результата
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    segments = [tuple(map(int, input().split())) for _ in range(n)]
    print(binary_search(segments))
