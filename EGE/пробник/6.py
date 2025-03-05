from turtle import *

"""
URL: https://education.yandex.ru/ege/task/c3a8e69d-de95-4f47-b562-6b78cf380369

"""


def main():
    tracer(0)
    left(90)
    speed(10000)
    k = 15
    for _ in range(2):
        forward(21 * k)
        right(90)
        forward(27 * k)
        right(90)
    pu()
    forward(9 * k)
    right(90)
    forward(10 * k)
    left(90)
    pd()
    for _ in range(2):
        forward(86 * k)
        right(90)
        forward(47 * k)
        right(90)
    pu()
    for x in range(-10 * k, 10 * k):
        for y in range(-10 * k, 10 * k):
            setpos(x * k, y * k)
            dot(2, 'red')
    done()


if __name__ == "__main__":
    main()
