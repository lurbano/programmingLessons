
# Find the distance between two points
def distTwoPoints(x1, y1, x2, y2):
    d = ( (x2-x1)**2 + (y2-y1)**2 )**0.5
    return d

# Find the midpoint between two points
def midpoint(x1, y1, x2, y2):
    x = (x2 + x1) / 2
    y = (y2 + y1) / 2
    return (x, y)


# Main Program
(x1, y1) = (7, 13)
(x2, y2) = (8, 14)

dist = distTwoPoints(x1, y1, x2, y2)
print("Distance =", dist)

print("Midpoint = ", midpoint(x1, y1, x2, y2))
