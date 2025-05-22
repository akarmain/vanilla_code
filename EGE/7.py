from math import log2


def task_kompege_22346():
    # Исходные параметры:
    freq1 = 30000  # Гц
    bitrate1 = 10  # бит
    duration1 = 150  # сек
    channels1 = 2
    tracks = 12

    # Сжатые параметры:
    freq2 = 30000 / 1.5  # = 20000
    bitrate2 = 10 / 5  # = 2
    duration2 = 150 / 3  # = 50
    channels2 = 2 / 2  # = templates1.ipynb

    # Скорость канала:
    speed = 140_000  # бит/с

    # Вычисляем объем данных до и после:
    volume1 = freq1 * bitrate1 * duration1 * channels1 * tracks
    volume2 = freq2 * bitrate2 * duration2 * channels2 * tracks

    # Время передачи в секундах:
    t1 = volume1 / speed
    t2 = volume2 / speed

    # Экономия во времени:
    time_saved = t1 - t2

    # Переводим в часы:
    return int(time_saved // 3600)


def task_yandex_0():
    "https://education.yandex.ru/ege/task/69f7445f-bff9-4586-bd5b-1bbfa80ff30d"
    return int((90 * 2 * 16 * 48000) / 3200)


def task_yandex_1():
    "https://education.yandex.ru/ege/task/6eb7bf36-3850-44e1-93fc-c1ba9edd9dc1"
    return 2 ** int((735 * 2 ** 13) / (315 * 3072))


def task_yandex_2():
    "https://education.yandex.ru/ege/task/4e5be1a0-54c9-454c-819a-0f8b27b8c0e6"
    h = ((50 * 155) / 100) * 2 ** 13
    return 2 ** int(h / (320 * 512))


def task_kompege_10709():
    f = 1920 * 1080 * log2(4096)
    return int((f * 68) / 2 ** 13)


def task_kompege_8944():
    f = 3 * 1024 * 1024 * 8
    d1 = (f * 100) / 80
    d2 = (f * 120) / 100
    print(int(log2(d1 / (1080 * 920))))
    print(int(log2(d2 / (1080 * 920))))
    # return int((f*68) / 2**13)


def task_kompege_8465():
    f1 = 1600 * 1920 * 8
    f2 = 32_000 * 8 * 4 * 104
    return int((f1 + f2) / (100 * (2 ** 13)))


def task_kompege_6014():
    return 128 / 4


def task_kompege_20364():
    ans = ((1920 * 1080 * 16) +
           (3600 * 16))
    return int((ans * 300*2) / (1024 * 1014 * 8))


if __name__ == "__main__":
    # print("ANS_task_kompege_22346", task_kompege_22346())
    # print("ANS_task_yandex_0:", task_yandex_0())
    # print("ANS_task_yandex_1:", task_yandex_1())
    # print("ANS_task_yandex_1:", task_yandex_2())
    # print("ANS_task_kompege_10709", task_kompege_10709())
    print("ANS_task_kompege_8944", task_kompege_8944())
    print("ANS_task_kompege_8465", task_kompege_8465())
    print("ANS_task_kompege_6014", task_kompege_6014())
    print("ANS_task_kompege_20364", task_kompege_20364())
