


for t in xrange(input()):
    n, k = map(int, raw_input().split())

    if k == 0:
        print ' '.join(map(str, xrange(1, n+1)))

    elif not n & 1 and not n % (2*k):
        for i in xrange(1, n+1):
            if ((i - 1) / k) & 1:
                print i - k,
            else:
                print i + k,
        print

    else:
        print -1

