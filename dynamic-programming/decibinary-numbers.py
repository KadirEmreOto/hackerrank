from bisect import bisect_left

maxn = 3*10**5

dp = [[0]*(maxn + 5) for i in xrange(20)]
sp = [[0]*(maxn + 5 )for i in xrange(20)]
ct = [0] * (maxn + 5)
st = [0] * (maxn + 5)
st[0] = 1

for i in xrange(1, 10):
    dp[1][i] = 1
    ct[i] += 1

for i in xrange(19):
    for j in xrange(maxn):
        for k in xrange(10):
            p = (j << 1) + k
            if p < maxn:
                dp[i+1][p] += dp[i][j]
                ct[p] += dp[i][j]

for i in xrange(20):
    for j in xrange(maxn):
        if j == 0: sp[i][j] = 1
        else: sp[i][j] = sp[i-1][j] + dp[i][j]

for i in xrange(1, maxn):
    st[i] = ct[i] + st[i-1]

for t in xrange(int(raw_input())):
    n = int(raw_input())

    if n == 1: print (0); continue
    i = bisect_left(st, n) - 1
    n -= st[i]

    for w in xrange(20):
        if dp[w][i+1] >= n or (1 << w > i + 1):
            break
        n -= dp[w][i+1]

    l = i + 1

    ans = ''
    for x in xrange(1, w+1):
        for y in xrange(10):
            if x == 1 and y == 0:
                continue

            sh = (1<<(w-x))
            t = n - sp[w-x][l - (sh*y)]

            if l == (sh*y):
                l -= (sh*y)
                ans += str(y)
                break

            elif t > 0:
                n = t
            else:
                l -= (sh*y)
                ans += str(y)
                break

    print(ans)


