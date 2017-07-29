from random import randint

def logical(i, j, k):
    if k <= 1: return 0

    d = 0
    for x in xrange(k-1):
        for y in xrange(x+1, k):
            d += g[i+x][j] > g[i+y][j];

    for x in xrange(k-1):
        for y in xrange(x+1, k):
            d += g[i+x][j+k-1] > g[i+y][j+k-1]

    d += logical(i - 1, j - 1, k - 2)

    return d - k+1

def rotate(i, j, k):
    if k <= 1: return

    a = []
    for y in xrange(j, j+k): a.append(g[i][y])
    for x in xrange(i+1, i+k-1): a.append(g[x][j+k-1])
    for y in xrange(j+k-1, j-1, -1): a.append(g[i+k-1][y])
    for x in xrange(i+k-2, i, -1): a.append(g[x][j])

    a = a[-k+1:] + a[:-k+1]

    t = 0
    for y in xrange(j, j+k): g[i][y] = a[t]; t += 1
    for x in xrange(i+1, i+k-1): g[x][j+k-1] = a[t]; t += 1
    for y in xrange(j+k-1, j-1, -1): g[i+k-1][y] = a[t]; t += 1
    for x in xrange(i+k-2, i, -1): g[x][j] = a[t]; t += 1

    rotate(i+1, j+1, k-2)

n = int(raw_input())
g = [map(int, raw_input().split()) for i in xrange(n)]
chance = lambda x: x >= randint(0, 100)
r = []
for i in xrange(4000):
    if len(r) == 500: break

    good = 0
    x = None
    for m in xrange(100):
        i = randint(0, n-2)
        j = randint(0, n-2)

        k = randint(2,3)

        if min(n-i, n-j) < k: continue

        ll = logical(i, j, k)
        if ll >= good:
            good = ll
            x, y, z = i, j, k

    if x is not None:
        r.append((x, y, z))
        rotate(x, y, z)

print len(r)
for i, j, k in r:
    print i+1, j+1, k




