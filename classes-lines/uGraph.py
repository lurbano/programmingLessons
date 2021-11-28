from vpython import *

def drawAxes():
    xaxis = curve(pos=[vec(-10,0,0), vec(10,0,0)])
    yaxis = curve(pos=[vec(0,-10,0), vec(0,10,0)])

    ticSize = 0.2
    for x in range(-10, 11):
        tic = curve(pos=[vec(x,ticSize,0), vec(x,-ticSize,0)])
    for y in range(-10, 11):
        tic = curve(pos=[vec(ticSize,y,0), vec(-ticSize,y,0)])

def plotPoints(pts, drawLine=False, r=0.2):
    if drawLine:
        c = curve(color=color.yellow)
    for p in pts:
        sphere(pos=p, radius=r, color=color.yellow)
        if drawLine:
            c.append(pos=p)

class uGraph:

    def __init__(self, xmin=-10, xmax=10, ymin=-10, ymax=10, drawTics=True, dTick=1, drawGrid=True):

        (self.xmin, self.xmax) = (xmin, xmax)
        (self.ymin, self.ymax) = (ymin, ymax)
        self.dTick = dTick
        xaxis = curve(pos=[vec(xmin,0,0), vec(xmax,0,0)])
        yaxis = curve(pos=[vec(0,ymin,0), vec(0,ymax,0)])

        if drawTics:
            ticSize = 0.2
            for x in arange(xmin, xmax+dTick):
                tic = curve(pos=[vec(x,ticSize,0), vec(x,-ticSize,0)])
            for y in range(ymin, ymax+dTick):
                tic = curve(pos=[vec(ticSize,y,0), vec(-ticSize,y,0)])

        if drawGrid:
            gridRadius= 0.05
            gridColor = vec(1,1,1)*0.5
            for x in arange(xmin, xmax+dTick):
                tic = curve(pos=[vec(x,ymax,0), vec(x,ymin,0)], radius=gridRadius, color=gridColor)
            for y in range(ymin, ymax+dTick):
                tic = curve(pos=[vec(xmax,y,0), vec(xmin,y,0)], radius=gridRadius, color=gridColor)

    def drawStraightLine(self, lineObj):
        ymin = lineObj.get_y(self.xmin)
        xmin = self.xmin
        if ymin < self.ymin:
            xmin = lineObj.get_x(self.ymin)
            ymin = lineObj.get_y(xmin)
        ymax = lineObj.get_y(self.xmax)
        xmax = self.xmax
        if ymax > self.ymax:
            xmax = lineObj.get_x(self.ymax)
            ymax = lineObj.get_y(xmax)

        p1 = vec(xmin, ymin, 0)
        p2 = vec(xmax, ymax, 0)
        line = curve(pos=[p1,p2])
        return line

    def plotPoints(self, pts, drawLine=False, r=0.2, col=color.yellow):
        if drawLine:
            c = curve(color=col)
        for p in pts:
            sphere(pos=p, radius=r, color=col)
            if drawLine:
                c.append(pos=p)
