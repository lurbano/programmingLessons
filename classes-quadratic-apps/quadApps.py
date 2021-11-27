
from vpython import *
from quad import *
from uGraph import *

drawAxes()

c = quadratic(0.5, 3, -5)
c.drawGraph()

x1 = -6
x2 = 2

y1 = c.get_y(x1)
y2 = c.get_y(x2)

p1 = vec(x1, y1, 0)
p2 = vec(x2, y2, 0)

print(f'for x = {x1}: point 1 = {p1}')
print(f'for x = {x2}: point 2 = {p2}')

plotPoints([p1, p2], drawLine=True)

distance = sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
print(f'Distance between point 1 and 2: {distance}')
