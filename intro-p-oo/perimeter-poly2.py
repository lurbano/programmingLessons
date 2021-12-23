import numpy as np

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

for i in np.arange(0, 2*np.pi,np.pi/3):
    x = 8*np.cos(i)
    y = 8*np.sin(i)
    print(i, x, y)

pts = []
pts.append(point(6,0))
pts.append(point(4,7))
pts.append(point(-7,4))
pts.append(point(-6,0))
pts.append(point(-7,-4))
pts.append(point(4,-7))

p = 0
for i in range(len(pts)-1):
    p += pts[i].distanceTo(pts[i+1])
    print(i, pts[i].x, pts[i].y, p)

p += pts[-1].distanceTo(pts[0])

print("Perimeter:", p)

# p1 = point(4,3)
# p2 = point(-4,7)
# p3 = point(-5,-4)
#
# tri = triangle(p1, p2, p3)
#
# # CALCULATIONS
# perimeter = tri.perimeter()
#
# # OUTPUT
# print("Perimeter: ", perimeter)
