
from bisect import *
n, k = map(int, raw_input().split())
a = map(int, raw_input().split())

h = k >> 1
p = a[:k]; p.sort()
answer = 0
for i in xrange(k, n):
    if k & 1:
        m = p[h]
    else:
        m = (p[h] + p[h-1]) >> 1
        if p[h]+p[h-1] & 1: m += 0.5

    if a[i] >= 2*m: answer += 1
    del p[bisect(p, a[i-k])-1]
    #p.remove(a[i-k])
    insort(p, a[i])
print answer

