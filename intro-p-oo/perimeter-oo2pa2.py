# CLASSES
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Method to find the distance to another point (p)
    def distanceTo(self, p):
        d = ((self.x-p.x)**2 + (self.y-p.y)**2)**0.5
        return d

# Triangle class that takes three vertices as point class instances.
class triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        p = self.p1.distanceTo(self.p2)
        p += self.p2.distanceTo(self.p3)
        p += self.p3.distanceTo(self.p1)
        return p

    def area(self):
        # using heron's formula
        a = abs(self.p1.distanceTo(self.p2))
        b = abs(self.p2.distanceTo(self.p3))
        c = abs(self.p3.distanceTo(self.p1))
        
        s = (a + b + c) / 2

        A = (s*(s-a)*(s-b)*(s-c))**0.5
        return A

# INPUT
pts = []
pts.append(point(6,0))
pts.append(point(4,7))
pts.append(point(4,-7))
pts.append(point(-6,0))
pts.append(point(-4,-7))
pts.append(point(4,-7))

p0 = point(0,0)

tris = []
for i in range(len(pts)-1):
    tris.append(triangle(pts[i], pts[i+1], p0))
    print(i)

tris.append(triangle(pts[5], pts[0], p0))

A = 0
for t in tris:
    area = t.area()
    A += area
    print(area)

# CALCULATIONS

# OUTPUT

print("Area:", A)
