from turtle import *

tracer(0)
left(90)
screensize(10000, 10000)
k = 10

for _ in range(6):
    forward(10 * k)
    right(90)
pu()

for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * k, y * k)
        dot(2, 'red')
done()
