from straightLine import *

line1 = straightLine(2, 1)

print("For y = 11, y =", line1.get_x(11))
print("Slope =", line1.slope)
print("perpendicular slope = ", line1.perpSlope())

print(line1.onLine(5,11))
