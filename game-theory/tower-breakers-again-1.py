
def grundy(limit=10**5+5):
    result = [0] * limit

    for i in xrange(2, limit):
        s = set([])
        for j in xrange(1, int(i**0.5)+1):
            d, r = divmod(i, j)

            if r == 0:
                if j & 1: s.add(result[d])
                if d & 1: s.add(result[j])

        j = 0
        while j in s: j += 1
        result[i] = j

    return result

g = grundy()

T = int(raw_input())
for t in xrange(T):
    n = int(raw_input())
    a = map(int, raw_input().split())
    r = 0

    for i in a: r ^= g[i]
    if r: print 1
    else: print 2

