
from pprint import pprint

n = int(raw_input())
a = map(int, raw_input().split())
d = [[0] * 101 for i in xrange(n)]

d[0][a[0]] = 1

for i in xrange(1, n):
    for j in xrange(101):
        if d[i - 1][j]:
            d[i][(j * a[i]) % 101] = '*'
            d[i][(j - a[i]) % 101] = '-'
            d[i][(j + a[i]) % 101] = '+'

m = 0
t = []
for i in xrange(n-1, 0, -1):
    t.append(d[i][m])

    if d[i][m] == '-': m += a[i]
    elif d[i][m] == '+': m -= a[i]
    elif d[i][m] == '*':
        while m % a[i]:
            m += 101
        m /= a[i]
    m %= 101

ans = ""
for i in xrange(n):
    ans += str(a[i])
    if i != n-1:
        ans += t[-i-1]

print ans

