def create_time_array(step):
    time_array = []
    current_time = 8 * 60
    while current_time <= 22 * 60:
        time_array.append(current_time)
        hours, minutes = divmod(current_time, 60)
        current_time = hours * 60 + minutes + step
    return time_array


def find_closest_time(input_time, time_array):
    # Переводим входное время в минуты от полуночи
    input_minutes = input_time[0] * 60 + input_time[1]

    # Инициализируем переменные для хранения ближайшего времени и разницы
    closest_time = None
    min_difference = float('inf')

    for time_minutes in time_array:
        if time_minutes < input_minutes:
            difference = input_minutes - time_minutes
            if difference < min_difference:
                min_difference = difference
                closest_time = time_minutes

    if closest_time is not None:
        hours, minutes = divmod(closest_time, 60)
        return (hours, minutes)
    else:
        return None


def time_difference(start_time, end_time):
    # Преобразовать начальное и конечное время в минуты с полуночи
    start_minutes = start_time[0] * 60 + start_time[1]
    end_minutes = end_time[0] * 60 + end_time[1]

    # Найти разницу между временами
    time_diff = abs(end_minutes - start_minutes)

    # Преобразовать разницу обратно в часы и минуты
    hours, minutes = divmod(time_diff, 60)

    return f"{hours:02d}:{minutes:02d}"


def main():
    h, m, a, b = map(int, input().split())
    a_arr = create_time_array(a)
    b_arr = create_time_array(b)
    for time_minutes in a_arr:
        hours, minutes = divmod(time_minutes, 60)
        print(f"{h}:{m} -> {hours:02d}:{minutes:02d} ({time_minutes - h*60 - m})")
    print()
    print()
    print()
    print()
    print()
    for time_minutes in b_arr:
        hours, minutes = divmod(time_minutes, 60)
        print(f"{h}:{m} -> {hours:02d}:{minutes:02d} ({time_minutes - h*60 - m})")


if __name__ == '__main__':
    main()
