from vpython import *

class straightLine:

def __init__(self, m, b):
self.m = m
self.b = b

self.slope = m
self.yintercept = b
self.xintercept = -b/m

def get_y(self, x):
y = self.m * x + self.b
return y

# method to get x given y
def get_x(self, y):
x = (y - self.b) / self.m
return x

line1 = straightLine(2, 1)

print("For y = 11, y =", line1.get_x(11))


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
