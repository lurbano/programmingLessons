from vpython import *

graphX = -5
graphY = 5
xaxis = curve(pos=[vec(-graphX,0,0), vec(graphX,0,0)])
yaxis = curve(pos=[vec(0,-graphY,0), vec(0,graphY,0)])

dx = 0.5
for x in range(5):
    for y in range(5):
        dy = 2 * dx
        arrow(pos=vec(x,y,0), axis=vec(dx, dy,0))
