import numpy as np
import random as rand

n = 10
noRepeats = True

m = 2
b = -5

x = []
y = []

while len(x) < n:
    v = rand.randint(-10, 10)
    l_repeated = False
    if noRepeats:
        for j in x:
            if v == j:
                l_repeated = True
    if not l_repeated:
        x.append(v)
        y.append(m*x[-1]+b)

print("x =", x)
print("y =", y)
