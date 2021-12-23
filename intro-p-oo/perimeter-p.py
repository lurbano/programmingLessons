# INPUT
p1_x = 4
p1_y = 3
p2_x = -4
p2_y = 7
p3_x = -5
p3_y = -4

# CALCULATIONS
# distance between (1) and (2)
side1 = ((p2_x - p1_x)**2 + (p2_y - p1_y)**2)**0.5

# distance between (2) and (3)
side2 = ((p3_x - p2_x)**2 + (p3_y - p2_y)**2)**0.5

# distance between (3) and (1)
side3 = ((p1_x - p3_x)**2 + (p1_y - p3_y)**2)**0.5

# Perimeter = total distance
perimeter = side1 + side2 + side3


# OUTPUT
print("Perimeter: ", perimeter)
