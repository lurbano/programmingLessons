from vpython import *

def drawAxes():
    xaxis = curve(pos=[vec(-10,0,0), vec(10,0,0)])
    yaxis = curve(pos=[vec(0,-10,0), vec(0,10,0)])

    ticSize = 0.2
    for x in range(-10, 11):
        tic = curve(pos=[vec(x,ticSize,0), vec(x,-ticSize,0)])
    for y in range(-10, 11):
        tic = curve(pos=[vec(ticSize,y,0), vec(-ticSize,y,0)])

def plotPoints(pts, drawLine=False):
    # input as vectors
    if drawLine:
        c = curve()
    r = 0.2
    for p in pts:
        sphere(pos=p, radius=r)
        if drawLine:
            c.append(pos=p)
