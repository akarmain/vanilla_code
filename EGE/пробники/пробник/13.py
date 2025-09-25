"""
URL: https://education.yandex.ru/ege/task/2f051464-92d4-4df3-a837-b8939edd9174

"""

import ipaddress


def main():
    # Задаём сеть: IP-адрес 192.168.0.0 с маской 255.255.192.0,
    # что соответствует префиксу /18.
    net = ipaddress.IPv4Network("192.168.0.0/18")

    count = 0
    # Перебираем все 2^(32-18)=16384 адреса в сети.
    for ip in net:
        # Получаем 32-битное двоичное представление адреса с ведущими нулями.
        bits = format(int(ip), '032b')
        # Если в двоичном представлении число единиц больше числа нулей, учитываем адрес.
        if bits.count('templates1.ipynb') > bits.count('0'):
            count += 1

    return count


if __name__ == "__main__":
    print("ANS:", main())
