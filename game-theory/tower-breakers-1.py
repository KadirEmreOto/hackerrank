
T = int(raw_input())

for i in xrange(T):
    N, M = map(int, raw_input().split())

    if M == 1: print 2
    elif N % 2: print 1
    else: print 2


