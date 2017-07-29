
def comp(e):
    return (e - 1) * e  / 2

for _ in xrange(int(raw_input())):
    n, m, s = map(int, raw_input().split())
    e = n-1
    m -= e

    a1 = s
    a1 += min(comp(e - 1), m)
    if m > comp(e - 1):
        a1 += (m - comp(e-1)) * (s - (e-1))

    a2 = s
    a2 += min(comp(e - 1), m) * (s / e)
    if m > comp(e - 1):
        a2 += (m - comp(e-1)) * ((s / e) + s % e)

    r = (e - (s%e))
    t = s / e
    if s % e: t += 1
    a3 = s
    a3 += comp(r) * (s / e)
    if m > comp(r):
        a3 += (m - comp(r)) * (t)

    print min(a1, a2, a3)


