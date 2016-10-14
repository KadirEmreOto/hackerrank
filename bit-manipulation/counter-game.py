

T = int(raw_input())
for t in xrange(1, T+1):
    N = int(raw_input())

    N = bin(N)[2:]
    M = N.rstrip('0')

    ans = len(N) - len(M)
    ans += M.count('1')

    if ans % 2: print 'Richard'
    else: print 'Louise'

