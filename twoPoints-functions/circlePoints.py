from vpython import *

def slope(x1, y1, x2, y2):
    s = (y2 - y1) / (x2 - x1)
    return s

def slopeVectors(v1, v2):
    s = (v2.y - v1.y) / (v2.x - v1.x)
    return s

def distance(v1, v2):
    d = sqrt((v2.x-v1.x)+(v2.y-v1.y))
    return d

circleRadius = 5
nNodes = 24

xaxis = curve(pos=[vec(-10,0,0), vec(10,0,0)])
yaxis = curve(pos=[vec(0,-10,0), vec(0,10,0)])

pts = []

dAngle = 360. / nNodes
for i in range(nNodes):
    x = circleRadius * cos(radians(dAngle*i))
    y = circleRadius * sin(radians(dAngle*i))
    pts.append(vec(x,y,0))

pts.append(pts[0])
line = curve()

for p in pts:
    sphere(pos=p, radius=0.25, color=color.yellow)
    line.append(p)
