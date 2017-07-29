mod = 10**9 + 7
n, m = map(int, raw_input().split())
count = it = pow(2, m, mod) - 1

F = 1
S = 0
N = 0

for i in xrange(2, n + 1):
    N = (it - S - F * (count - i + 2) * (i - 1)) % mod
    it = (it * (count - i + 1)) % mod
    F = S
    S = N

print (it - N) % mod


