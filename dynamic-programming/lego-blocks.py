
def f(i):
    if i in df: return df[i]
    if i == 0: return 1
    if i < 0: return 0

    a = f(i-1) + f(i-2) + f(i-3) + f(i-4)
    df[i] = a
    return a

def g(i):
    if i in dg: return dg[i]
    a = pow(f(i), n, mod)
    dg[i] = a
    return a

def h(i):
    if i == 1: return 1
    if i in dh: return dh[i]
    a = g(i)

    for j in xrange(1, i):
        a -= h(j) * g(i - j) % mod

    dh[i] = a % mod
    return a % mod

mod = 10**9 + 7
for i in xrange(input()):
    n, m = map(int, raw_input().split())

    df = {}
    dg = {}
    dh = {}
    print h(m)


