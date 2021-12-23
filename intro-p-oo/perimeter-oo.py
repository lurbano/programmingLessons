# CLASSES 
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Method to find the distance to another point (p)
    def distanceTo(self, p):
        d = ((self.x-p.x)**2 + (self.y-p.y)**2)**0.5
        return d

# INPUT
p1 = point(4,3)
p2 = point(-4,7)
p3 = point(-5,-4)

# CALCULATIONS
# distance between (1) and (2)
side1 = p1.distanceTo(p2)

# distance between (2) and (3)
side2 = p2.distanceTo(p3)

# distance between (3) and (1)
side3 = p3.distanceTo(p1)

# Perimeter = total distance
perimeter = side1 + side2 + side3


# OUTPUT
print("Perimeter: ", perimeter)
