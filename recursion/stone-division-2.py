
def solve(y):
    ans = 0
    if y in dp: return dp[y]

    for x in a:
        d, r = divmod(y, x)
        if d == 0:
            break

        if r == 0 and y != x:
            ans = max(ans, d * solve(x) + 1)

    dp[y] = ans
    return ans


for i in xrange(int(raw_input())):
    n, m = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()

    dp = dict()
    print solve(n)

