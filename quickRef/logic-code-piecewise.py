from vpython import *

xaxis = curve(pos=[vec(0,10,0), vec(0,-10,0)])
xaxis = curve(pos=[vec(10,0,0), vec(-10,0,0)])

for x in arange(-10, 10, 0.1):
    if x < -2:
        y = x
        col = color.red
    elif x < 3:
        y = 2*x-1
        col = color.green
    else:
        y = -1
        col = color.yellow

    sphere(pos=vec(x,y,0), radius=0.1, color=col)
