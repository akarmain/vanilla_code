from turtle import *
tracer(0)
left(90)
speed(10000)
k = 5
for _ in range(7):
	for _ in range(7):
	    forward(180*k)
	    rigth(120)
	rigth(120)
rigth(120)
forward(15)
rigth(90)
forward(360)
rigth(90)
forward(15)
rigth(30)
forward(74)

for x in range(-10, 15):
    for y in range(-4, 13):
        setpos(x * k, y * k)
        dot(2, 'red')
done()
