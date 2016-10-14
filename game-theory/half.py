from math import log

gnum = {}
def grundy(x):
    if x not in gnum:
        gnum[x] = int(log(x, 2)) + 1
    return gnum[x]

T = int(raw_input())
for t in xrange(1, T+1):
    N = int(raw_input())

    if N % 2: print 1; continue
    a = grundy(N)

    b = 2 ** int(log(a, 2))
    s = a ^ b ^ 1

    r = 2 ** (b - 1)
    l = 2 ** s - 1

    if r - l < r / 2: print r / 2
    else: print r - l

