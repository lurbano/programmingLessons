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
