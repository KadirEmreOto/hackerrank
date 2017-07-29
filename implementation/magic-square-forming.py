from copy import deepcopy

P = (
    ((8, 1, 6), (3, 5, 7), (4, 9, 2)),
    ((6, 1, 8), (7, 5, 3), (2, 9, 4)),
    ((4, 9, 2), (3, 5, 7), (8, 1, 6)),
    ((2, 9, 4), (7, 5, 3), (6, 1, 8)),
    ((8, 3, 4), (1, 5, 9), (6, 7, 2)),
    ((4, 3, 8), (9, 5, 1), (2, 7, 6)),
    ((6, 7, 2), (1, 5, 9), (8, 3, 4)),
    ((2, 7, 6), (9, 5, 1), (4, 3, 8))
    )

T = [map(int, raw_input().split()) for i in xrange(3)]

A = float('inf')
for p in P:
    a = 0
    for i in xrange(3):
        for j in xrange(3):
            a += abs(T[i][j] - p[i][j])    

    A = min(a, A)
print A

