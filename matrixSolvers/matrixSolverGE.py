import numpy as np

def solv_GE(data):
    print("Solving...")
    a = np.array(data, float)
    print(a)
    print()

    (r, c) = a.shape
    print(r,c)

    print(a)
    print()

    for i in range(0,r):
        a[i] = a[i] / a[i][i]
        for j in range(i+1, r):
            a[j] = a[j] - a[i]*a[j][i]

    print(a)
    print()

    for i in range(r-1):
        for j in range(i+1, r):
            a[i] = a[i] - a[j]*a[i][j]

    print(a)
    print()



n5 = [
        [4, 1, 2, 14660],
        [1, 1, 1, 9480],
        [1, 0, -2, 140]
]

n4 = [
        [2, 3, 5, 1240],
        [3,1,4,1027],
        [5,7,2,2091]
]
solv_GE(n4)
