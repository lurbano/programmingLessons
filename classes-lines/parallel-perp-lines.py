from straightLine import *
from uGraph import uGraph
from vpython import *

line1 = straightLine(3, -4)
p1 = vec(5,1,0)

graph = uGraph()
graph.drawStraightLine(line1)
graph.plotPoints([p1], r=0.3, col=color.green)

# draw parallel line
line_parallel = getLineFromSlopeAndPoint(line1.slope, p1)
graph.drawStraightLine(line_parallel)

# draw perpendicular line
line_perp = getLineFromSlopeAndPoint(line1.perpSlope(), p1)
graph.drawStraightLine(line_perp)
