
T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    if N % 7 in [0, 1]:
        print 'Second'
    else:
        print 'First'
