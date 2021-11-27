from vpython import *

class quad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_y(self, x):
        y = self.a * x**2 + self.b * x + self.c
        return y

    def vertex_x(self):
        x = -self.b/(2*self.a)
        return x

    def vertex_y(self):
        y = self.get_y(self.vertex_x())
        return y

    def printEqn(self):
        t = 'y = '
        if self.a != 0:
            if self.a != 1:
                t += str(self.a)
            t += 'x² '
        if self.b != 0:
            if self.b < 0:
                t += '- '
            else:
                t += '+ '
            if abs(self.b) != 1:
                t += str(abs(self.b))
            t += 'x '
        if self.c != 0:
            if self.c < 0:
                t += '- '
            else:
                t += '+ '
            t += str(abs(self.c))
        return t

    def getSlope(self, x):
        slope = 2 * self.a * x + self.b
        return slope

    def getYIntercept(self):
        return self.c

    def getZeros(self):
        x1 = (-self.b + (self.b**2 - (4*self.a*self.c))**0.5) / (2 * self.a)
        x2 = (-self.b - (self.b**2 - (4*self.a*self.c))**0.5) / (2 * self.a)
        return [x1, x2]

    def drawGraph(self):
        c = curve()
        dx = 0.1
        for x in arange(-10, 10+dx, dx):
            y = self.get_y(x)
            if y > -10 and y < 10:
                c.append(pos=vec(x,y,0))

    def areaX(self, x1, x2):
        a1 = (self.a * x1**3)/3.0 + (self.b * x1**2)/2.0 + self.c * x1
        a2 = (self.a * x2**3)/3.0 + (self.b * x2**2)/2.0 + self.c * x2
        A = a2 - a1
        return A



xaxis = curve(pos=[vec(-10,0,0), vec(10,0,0)])
yaxis = curve(pos=[vec(0,-10,0), vec(0,10,0)])

ticSize = 0.2
for x in range(-10, 11):
    tic = curve(pos=[vec(x,ticSize,0), vec(x,-ticSize,0)])
for y in range(-10, 11):
    tic = curve(pos=[vec(ticSize,y,0), vec(-ticSize,y,0)])

q = quad(1, 2, -8)
q.drawGraph()


#output
x = 3

print(f'For the equation: {q.printEqn()}')
print(f'(1) If x = {x} then y = {q.get_y(x)}')
print(f'(2) The x-coordinate of the vertex is {q.vertex_x()}')
print(f'(3) The y-coordinate of the vertex is {q.vertex_y()}')
print(f'(4) The (x, y) coordinates of the vertex are ({q.vertex_x()}, {q.vertex_y()})')
print(f'(5) The y-intercept is at y = {q.getYIntercept()}')
print(f'(6) The x intercepts (zeros) of the function are: {q.getZeros()}')
print(f'(7) The human readable form of the equation is: {q.printEqn()}')
print(f'(8) Drawing graph (see below) ...')
print(f'(9) The slope of the line at x = {q.vertex_x()}: dy/dx = {q.getSlope(q.vertex_x())}')
print(f'(9) The slope of the line at x = {x}: dy/dx = {q.getSlope(x)}')

(x1, x2) = (0, 2)
print(f'The area under the curve between {x1} and {x2} \n     is {q.areaX(x1, x2)}')
