
T = int(raw_input())

for t in xrange(T):
    N = int(raw_input())
    array = map(int, raw_input().split())

    ans = 0
    for i in xrange(N):
        if array[i] % 2:
            ans ^= i

    if ans: print 'First'
    else: print 'Second'
