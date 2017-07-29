from sys import setrecursionlimit; setrecursionlimit(10**6 + 5)
import resource; resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

mod = 10**9 + 7

fac = [1]
for i in xrange(1, 5005):
    fac.append((fac[-1] * i)%mod)

def solve(one, two):
    if one in dp and two in dp[one]:
        return dp[one][two]

    if one and two == 0:
        return fac[one]

    if one < 0 or two < 0:
        return 0

    if one == 0 and two == 1:
        return 0

    ans = one * solve(one - 1, two)
    ans += two * (solve(one + 1, two - 1) - solve(one, two - 1))

    if one not in dp:
        dp[one] = {}
    dp[one][two] = ans % mod
    return dp[one][two]

dp = {}

for _ in xrange(int(raw_input())):
    N = int(raw_input())
    A = map(int, raw_input().split())
    c = [0, 0]
    s = set()

    for i in A:
        if i in s:
            c[0] -= 1
            c[1] += 1

        else:
            c[0] += 1
        s.add(i)

    print solve(*c)

