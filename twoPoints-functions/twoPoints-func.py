from vpython import *

def slope(x1, y1, x2, y2):
    s = (y2 - y1) / (x2 - x1)
    return s

def slopeVectors(v1, v2):
    s = (v2.y - v1.y) / (v2.x - v1.x)
    return s

xaxis = curve(pos=[vec(-10,0,0), vec(10,0,0)])
yaxis = curve(pos=[vec(0,-10,0), vec(0,10,0)])

p1 = vec(-3,1,0)
p2 = vec(5,7,0)

s1 = sphere(pos=p1, radius=0.5, color=color.red)
s2 = sphere(pos=p2, radius=0.5, color=color.yellow)

line = curve(pos=[p1, p2])

print("Point 1:", p1.x, ",", p1.y)
print("Point 2:", p2.x, ",", p2.y)

m = slopeVectors(p1, p2)

print("The slope between the two points is:", m)
