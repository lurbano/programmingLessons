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

    def perpSlope(self):
        m_p = -1/self.slope
        return m_p

    def onLine(self, x, y):
        yCheck = self.get_y(x)
        if yCheck == y:
            return True
        else:
            return False

    def printEqn(self):
        if self.b == 0:
            print(f'y = {self.m} x ')
        elif (self.b > 0):
            print(f'y = {self.m} x + {self.b}')
        else:
            print(f'y = {self.m} x - {abs(self.b)}')

def getLineFromPoints(v1, v2):
    # input as vectors
    m = (v2.y - v1.y) / (v2.x - v1.x)
    b = v1.y - m * v1.x
    return straightLine(m, b)

def getLineFromSlopeAndPoint(m, v):
    b = v.y - m * v.x
    return straightLine(m, b)

def linesIntersect(l1, l2):
    x = (l2.b - l1.b) / (l1.m - l2.m)
    y = l1.m * x + l1.b
    return vec(x, y, 0)
