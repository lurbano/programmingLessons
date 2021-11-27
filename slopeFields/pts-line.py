# INPUT
#   Set the two points
(x1, y1) = (1, 2)
(x2, y2) = (5, 4)

# CALCULATIONS
#   calculate the changes in x and y
dx = x2 - x1
dy = y2 - y1

#   calculate the slope
slope = dy / dx

#   calculate the intercept
intercept = y1 - slope * x1

#OUTPUT
print("The slope is:", slope)
print("The intercept is:", intercept)
