"""
был дан для исполнения следующий алгоритм:
Повтори 2 Вперёд 8 Направо 90 Вперёд 18 Направо 90)
Поднять хвост
Вперёд 4 Направо 90 Вперёд 10 Налево 90
Опустить хвост
Повтори 2 [Вперёд 17 Направо 90 Вперёд 7 Направо 90]
Определите, сколько точек с целочисленными координатами заданными алгоритмом линиями, включая точки на линиях.
"""
import time
from turtle import *


def main():
    left(90)

    z= 10
    speed(999)
    for _ in range(2):
        forward(z*8)
        right(90)
        forward(z*18)
        right(90)
    up()
    for _ in range(4):
        right(90)
        forward(z * 10)
        left(90)
    down()
    for _ in range(2):
        forward(z*17)
        right(90)
        forward(z*7)
        right(90)

    down()
    time.sleep(1000)
    ...


if __name__ == "__main__":
    print("ANS:", main())
