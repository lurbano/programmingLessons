import numpy as np

# enter data in standard form
data = [
        [8, 5, 55.27],
        [6, 4, 42.70]
       ]

a = np.array(data)

print(a)

a[0] = a[0] / a[0,0]

print(a)

a[1] = a[0] * a[1,0] - a[1]

print(a)

a[1] = a[1] / a[1,1]

print(a)

a[0] = a[0] - a[1]*a[0,1]

print(a)
