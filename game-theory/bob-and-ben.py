
for i in xrange(input()):
    n = int(raw_input())

    a = 0
    for i in xrange(n):
        n, k = map(int, raw_input().split())

        if n == 1: a ^= 1
        elif n == 2: pass
        elif n & 1: a ^= 1
        else: a ^= 2

    print 'BOB' if a else 'BEN'


