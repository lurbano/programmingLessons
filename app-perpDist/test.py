from uGraph import *
from straightLine import *

p1 = vec(1, 5, 0)
p2 = vec(6, 0, 0)

p3 = vec(8, 6, 0)

d = findPerpendicularDistance(p1, p2, p3)

print(d)
