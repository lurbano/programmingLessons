from vpython import *

def f(x):
    y = x - 4
    return y

def h(x_in):
    y_out = x_in**2 / 12
    return y_out

def n(x):
    return abs((x**2/10)-2)

def drawFunction(f, col=color.white, dx=1):
    c = curve()
    for x in arange(-10,10,dx):
        y = f(x)
        sphere(pos=vec(x,y,0), radius=0.25, color=col)
        c.append(pos=vec(x,y,0), color=col)

xaxis = curve(pos=[vec(-10,0,0), vec(10,0,0)])
yaxis = curve(pos=[vec(0,-10,0), vec(0,10,0)])

# draw the functions:
#drawFunction(f)
#drawFunction(h, color.red)
drawFunction(n, color.yellow, 0.1)

# create curves
# line = curve()
# line1 = curve()
# line2 = curve()


# for x in range(-10, 10, 1):
#     y = h(x)
#     sphere(pos=vec(x,y,0), radius=0.25)
#     #append points to curve
#     line.append(pos=vec(x,y,0))
#
#     #draw equation 1
#     y = f(x)
#     sphere(pos=vec(x,y,0), radius=.25, color=color.red)
#     line1.append(pos=vec(x,y,0), color=color.red)
#
#     # combine equations
#     y = h(f(x))
#     sphere(pos=vec(x,y,0), radius=.25, color=color.green)
#     line2.append(pos=vec(x,y,0), color=color.green)
