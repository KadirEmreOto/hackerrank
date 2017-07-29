from math import log

def iterate(m):
    if m == 0: return
    global a

    t = []
    if m == 1:
        for i in xrange(n):
            t.append(a[i] ^ a[(i + 1) % n])
        a = t

    else:
        b = int(log(m, 2))
        e = 1 << b

        for i in xrange(n):
            t.append(a[i] ^ a[(i + e) % n])
        a = t
        iterate(m - e)

n, m = map(int, raw_input().split())
a = map(lambda x: ord(x) - 65, raw_input())

iterate(m)
print ''.join(map(lambda x: chr(x+65), a))

