
# Create Class: The class' name is "straightLine"
class straightLine:
    def __init__(self, m, b):     # initialize
        self.slope = m            # set properties
        self.y_intercept = b
        self.x_intercept = -b/m

    def get_y(self, x):
        y = self.slope * x + self.y_intercept
        return y

line_1 = straightLine(2, 3)     # create an instance for y = 2x + 3
line_2 = straightLine(-1, 4)    # create an instance for y = -x + 4

# Get y when x = 5 for line 2
print("For x = 5, y =", line_2.get_y(5))
print()

# get y values for both lines
print("x,y1,y2")
for i in range(5):
    print( i, line_1.get_y(i), line_2.get_y(i))
    #print("x =", i, ", y1 = ", line_1.get_y(i))
    #print("x =", i, ", y2 =", line_2.get_y(i))
    #print(f'x={i}, y1 = { line_1.get_y(i) }, y2 = { line_2.get_y(i) }')
