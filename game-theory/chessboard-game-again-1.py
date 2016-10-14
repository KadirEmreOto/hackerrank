
def find(i, j):
    if not (0 <= i < 15 and 0 <= j < 15): return
    if grundy[i][j] != None: return grundy[i][j]

    s = set([])
    s.add(find(i-2, j-1))
    s.add(find(i-2, j+1))
    s.add(find(i-1, j-2))
    s.add(find(i+1, j-2))

    for g in xrange(10):
        if g not in s:
            grundy[i][j] = g
            return g

grundy = [[None]*15 for i in xrange(15)]

T = int(raw_input())

for t in xrange(T):
    N = int(raw_input())
    answer = 0
    for i in xrange(N):
        x, y = map(int, raw_input().split())
        answer ^= find(y-1, x-1)
        
    if answer: print 'First'
    else: print 'Second'




