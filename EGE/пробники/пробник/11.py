"""
URL: https://education.yandex.ru/ege/task/932ea967-e8f2-4d30-98a4-b095b10e5b33
GPT
"""

import math


def main():
    total_serials = 506
    required_memory = 63 * 1024  # 63 Кбайт в байтах
    # Размер алфавита
    alphabet_size = 10 + 26 + 230  # 266
    # Бит на символ: минимальное k, такое что 2^k >= alphabet_size
    bits_per_symbol = 9  # поскольку 2^9 = 512 >= 266

    # Ищем минимальное L
    L = 1
    while True:
        bytes_per_serial = math.ceil((bits_per_symbol * L) / 8)
        total_bytes = total_serials * bytes_per_serial
        if total_bytes > required_memory:
            return L
        L += 1
    return L


if __name__ == "__main__":
    print("ANS:", main())
