
T = int(raw_input())
for t in xrange(1, T+1):
    N = int(raw_input())

    if N == 1: print 'Kitty'
    elif N & 1: print 'Katty'
    else: print 'Kitty'
