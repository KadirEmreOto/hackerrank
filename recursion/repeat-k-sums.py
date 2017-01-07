from collections import Counter
from sys import setrecursionlimit; setrecursionlimit(10 ** 6 + 5)
from resource import *; setrlimit(RLIMIT_STACK, (RLIM_INFINITY, RLIM_INFINITY))

def delete(j, s, c=1):
    if j < 0: return

    if c == k:
        csum[s] -= 1
    else:
        delete(j, s + ar[j], c+1)
        delete(j-1, s, c)

for _ in xrange(int(raw_input())):
    n, k = map(int, raw_input().split())
    ksum = map(int, raw_input().split())
    csum = Counter(ksum)

    ksum.sort()
    csum[ksum[0]] -= 1
    ar = [ksum[0] / k]

    i = 1
    while len(ar) < n:
        if csum[ksum[i]] > 0:
            ar.append(ksum[i] - ar[0]*(k-1))

            if len(ar) == n: break
            delete(len(ar)-1, ar[-1])

        i += 1

    print ' '.join(map(str, ar))

