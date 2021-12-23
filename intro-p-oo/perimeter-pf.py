# FUNCTIONS
def distance(x1, y1, x2, y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d

# INPUT
p1_x = 4
p1_y = 3
p2_x = -4
p2_y = 7
p3_x = -5
p3_y = -4

# CALCULATIONS
# distance between (1) and (2)
side1 = distance(p1_x, p1_y, p2_x, p2_y)

# distance between (2) and (3)
side2 = distance(p2_x, p2_y, p3_x, p3_y)

# distance between (3) and (1)
side3 = distance(p3_x, p3_y, p1_x, p1_y)

# Perimeter = total distance
perimeter = side1 + side2 + side3


# OUTPUT
print("Perimeter: ", perimeter)
