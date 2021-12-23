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
        a = self.p1.distanceTo(self.p2)
        b = self.p2.distanceTo(self.p3)
        c = self.p3.distanceTo(self.p1)

        s = (a + b + c) / 2

        A = (s*(s-a)*(s-b)*(s-c))**0.5
        return A

# INPUT
p1 = point(4,3)
p2 = point(-4,7)
p3 = point(-5,-4)

tri = triangle(p1, p2, p3)

# CALCULATIONS
perimeter = tri.perimeter()

# OUTPUT
print("Perimeter: ", perimeter)
print("Area:", tri.area())
