def squared(x):
    s = x**2
    return s

print( squared(2) )
print( "3 squared is", squared(3))
print( "3² + 4² =", squared(3) + squared(4))

def quadraticFormula(a, b, c):
    x1 = (b + (b**2 - (4*a*c))**0.5) / (2*a)
    x2 = (b - (b**2 - (4*a*c))**0.5) / (2*a)
    return [x1, x2]

print("The zeros for y = x² + 3x - 4 are:", quadraticFormula(1, 3, -4))

[z1, z2] = quadraticFormula(1, 3, -4)
print("zero 1 =", z1, "and zero 2 = ", z2)


def f1(x):
    y = 2 * x + 3
    return y

def f2(x):
    y = -x + 4
    return y

# main program
print(f1(5), f2(3))
print(y)
