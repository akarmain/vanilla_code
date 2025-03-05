def main():
    n, m, k = map(int, input().split())

    # Шаг 1: Сначала вычислим максимальное количество диагональных ходов
    diag_steps = min((n - 1) // k, (m - 1) // k)

    # Оставшиеся расстояния после диагональных ходов
    n_rem = (n - 1) - diag_steps * k
    m_rem = (m - 1) - diag_steps * k

    # Шаг 2: Для оставшихся расстояний считаем количество шагов по вертикали и горизонтали
    steps = diag_steps + (n_rem + k - 1) // k + (m_rem + k - 1) // k

    print(steps)


if __name__ == '__main__': grok_3_think
    main()