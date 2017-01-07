
def Solve(n, s, k, l=0):
    m = s % n
    if k < (m * (n-m)):
        return False

    if (n-1) * s < k: return False

    h = n + (s << 6) + (k << 14) + (l << 25)
    if n == 1:
        if k: return False
        dp[h] = s

    if h in dp:
        if dp[h] == -1: return False
        return True

    for i in xrange(l, s / n + 1):
        p = k - ((s-i)-i*(n-1))
        if p < 0:
            continue

        if Solve(n-1, s-i, p, i):
            dp[h] = i
            return True

    dp[h] = -1
    return False

dp = {}
for i in xrange(input()):
    n, s, k = map(int, raw_input().split())

    if Solve(n, s, k):
        i = 0
        h = n + (s << 6) + (k << 14) + (i << 25)
        while h in dp:
            #print (n, s, k, i), dp[(n, s, k, i)]
            i = dp[h]
            k -= ((s-i)-i*(n-1))
            n -= 1
            s -= i
            h = n + (s << 6) + (k << 14) + (i << 25)
            print i,
        print

    else:
        print -1


