import numpy as np

def solv_2x2(data):
    # data is a 2x3 list
    print("Solving...")
    a = np.array(data)
    print(a)
    print()

    a[0] = a[0] / a[0,0]
    print(a)
    print()

    a[1] = a[0] * a[1,0] - a[1]
    print(a)
    print()

    a[1] = a[1] / a[1,1]
    print(a)
    print()

    a[0] = a[0] - a[1]*a[0,1]
    print(a)

# enter data in standard form
data = [
        [8, 5, 55.27],
        [6, 4, 42.70]
       ]

n11 = [
        [.05, .1, 9.45],
        [.05, .2, 16.65]
       ]

n10 = [
        [25., 10., 180.],
        [1., 1., 12.]
       ]

n9 = [
        [8.,5.,55.27],
        [6.,4.,42.70]
]

n1 = [
        [4,3,10.93],
        [7,2,13.31]
]

solv_2x2(n1)
