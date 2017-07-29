
def check(c):
    m = float('inf')
    for i in xrange(n):
        if c & 1:
            if a[-i-1] > m:
                return False
            m = a[-i-1]
        c >>= 1
        if c == 0:
            break
    return True

def solve(c):
    if c in d:
        return d[c]

    if check(c):
        d[c] = False
        return False

    t = 1
    for i in xrange(15):
        if c & t:
            if not solve(c ^ t):
                d[c] = True
                return True
        t <<= 1

    d[c] = False
    return False

for _ in xrange(int(raw_input())):
    n = int(raw_input())
    a = map(int, raw_input().split())
    d = {}

    print 'Alice' if solve((1 << n) - 1) else 'Bob'

