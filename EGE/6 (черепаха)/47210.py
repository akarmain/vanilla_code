from turtle import *
tracer(0)
left(90)
speed(10000)
k = 30
for _ in range(7):
    forward(10*k)
    left(120)
pu()
for x in range(-10, 15):
    for y in range(-4, 13):
        setpos(x * k, y * k)
        dot(2, 'red')
done()
