import math

found = {-1: 0, 0: 0, 1: 1}

def Find(n):
    if n in found: return found[n]

    log = int(math.log(n, 2))
    po2 = 1 << log

    answer = Find(po2-1) + (n-po2+1) + Find(n-po2)
    found[n] = answer
    return answer

T = int(raw_input())
for t in xrange(T):
    a, b = map(int, raw_input().split())
    a, b = min(a, b), max(a, b)

    if a < 0:
        if b >= 0:
            print 32 * abs(a) - Find(abs(a) - 1) + Find(b)

        else:
            a = 32 * abs(a) - Find(abs(a) - 1)
            b = 32 * abs(b+1) - Find(abs(b+1) - 1)

            print a - b
    else:
        print Find(b) - Find(a-1)

