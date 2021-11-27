from vpython import *
from straightLine import *
from uGraph import *

def distancePts(p1, p2):
    d = sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
    return d

p1 = vec(1, 5, 0)
p2 = vec(6, 0, 0)

p3 = vec(8, 6, 0)

drawAxes()
plotPoints([p1, p2], drawLine=True)

line1 = getLineFromPoints(p1, p2)
line1.printEqn()

pSlope = line1.perpSlope()

line2 = getLineFromSlopeAndPoint(pSlope, p3)
line2.printEqn()

p4 = linesIntersect(line1, line2)
print(p4)

plotPoints([p3,p4], drawLine=True)

dist = distancePts(p3, p4)

print("Perpendicular Distance =", dist)

# print("For y = 11, y =", line1.get_x(11))
# print("Slope =", line1.slope)
# print("perpendicular slope = ", line1.perpSlope())
#
# print(line1.onLine(5,11))
