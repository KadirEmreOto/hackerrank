from __future__ import print_function

N, Q = map(int, raw_input().split())

A = raw_input()
B = raw_input()
C = int(A, 2) + int(B, 2)

A = list(A[::-1])
B = list(B[::-1])

dp = [1]

for i in xrange(Q):
    line = raw_input().split()

    if line[0] == 'set_a':
        idx, x = int(line[1]), line[2]
        if x != A[idx]:
            if x == '0':
                C -= 1 << idx
                A[idx] = '0'
            else:
                C += 1 << idx
                A[idx] = '1'

    elif line[0] == 'set_b':
        idx, x = int(line[1]), line[2]
        if x != B[idx]:
            if x == '0':
                C -= 1 << idx
                B[idx] = '0'
            else:
                C += 1 << idx
                B[idx] = '1'

    else:
        idx = int(line[1])
        ans = C & 1 << idx
        if ans: ans = 1
        print(ans, sep='', end='')

