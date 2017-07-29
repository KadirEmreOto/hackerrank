
for i in xrange(int(raw_input())):
    n = int(raw_input())
    a = [map(int, raw_input().split()) for i in xrange(n)]

    s = map(sum, a)
    t = [0] * n
    for j in xrange(n):
        for i in xrange(n):
            t[j] += a[i][j]

    s.sort()
    t.sort()

    if s != t:
        print 'Impossible'

    else:
        print 'Possible'

