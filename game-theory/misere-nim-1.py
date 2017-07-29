
for i in xrange(int(raw_input())):
    n = int(raw_input())
    a = map(int, raw_input().split())
    s = reduce(lambda x, y: x ^ y, a, 0)
    o = len(set(a)) == 1 and a[0] == 1

    print 'Second' if (o and n & 1 == 1) or (not o and not s) else 'First'

