
MOD = 10**9 + 7
INV2 = pow(2, MOD - 2, MOD)
t = 1 << 16

def transform(l, r):
    if l == r-1: return

    d = (r - l) >> 1
    m = l + d

    transform(l, m)
    transform(m, r)

    for i in xrange(l, m):
        x1 = a[i]
        x2 = a[i+d]
        a[i] = (x1 - x2 + MOD) % MOD
        a[i+d] = (x1 + x2) % MOD

def untransform(l, r):
    if l == r - 1: return

    d = (r - l) >> 1
    m = l + d

    for i in xrange(l, m):
        y1 = a[i]
        y2 = a[i+d]
        a[i] = ((y1 + y2) * INV2) % MOD
        a[i+d] = ((y2 - y1 + MOD) * INV2) % MOD

    untransform(l, m)
    untransform(m, r)

a = [0] * (1<<16)
arr = [0] * (10**5 + 5)
n = int(raw_input())

for i in xrange(1, n+1):
    arr[i] = int(raw_input()) ^ arr[i-1]
    a[arr[i]] += 1

transform(0, t)
for i in xrange(t): a[i] = pow(a[i], 2, MOD)
untransform(0, t)
a[0] -= n
for i in xrange(t): a[i] >>= 1
for i in xrange(1, n+1): a[arr[i]] += 1

l = 0
m = 0

for i in xrange(t):
    if a[i] > m:
        m = a[i]
        l = i

print l, m

