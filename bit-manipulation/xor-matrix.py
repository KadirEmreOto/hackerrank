
def iterate(times):
    if times <= 0: return
    global a

    t = []
    if times == 1:
        for i in xrange(n):
            t.append(a[i] ^ a[(i + 1) % n])
        a = t

    else:
        b = len(bin(times)) - 3
        e = 1 << b

        for i in xrange(n):
            t.append(a[i] ^ a[(i + e) % n])
        a = t
        iterate(times - e)

n, m = map(int, raw_input().split())
a = map(int, raw_input().split())

iterate(m-1)
print ' '.join(map(str, a))

