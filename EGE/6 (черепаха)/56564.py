from turtle import *

# Повтори 3 [Вперёд 7 Направо 90]
# Вперёд 8
# Повтори 3 [Налево 90 Вперёд 5].
# Определите, сколько различных точек с целочисленными координатами будет находиться на линиях, полученных при выполнении данной программы.
left(90)
speed(1000)
pendown()
k = 20

for i in range(3):
    forward(7 * k)
    right(90)

forward(8 * k)

for i in range(3):
    left(90)
    forward(5 * k)
penup()
for x in range(-1, 10):
    for y in range(-7, 10):
        setpos(x * k, y * k)
        dot(4)

done()
# 43
