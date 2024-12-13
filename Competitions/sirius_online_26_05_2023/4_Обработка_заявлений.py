def process_statements(N, K):
    step = 1  # текущий шаг
    remaining_statements = N  # оставшееся количество заявлений

    while remaining_statements > 0:
        if K == 1 and step % 3 != 0:
            return "Yes", step
        elif K % 2 == 0 and K <= remaining_statements:
            return "No", step

        # Вычисляем количество выбрасываемых и кладущихся заявлений
        discarded = remaining_statements // 2
        put_down = remaining_statements // 3

        # Если заявление K выбрасывается или кладется, корректируем его номер
        if K <= discarded or K <= put_down:
            K -= discarded

        # Обновляем оставшееся количество заявлений
        remaining_statements -= discarded
        remaining_statements += put_down

        step += 1

    return "No", step

# Считываем входные данные
N = int(input())
K = int(input())

# Вызываем функцию для обработки заявлений
result = process_statements(N, K)

# Выводим результат
print(result[0])
print(result[1])
