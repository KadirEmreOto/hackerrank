
n = int(raw_input())
a = map(int, raw_input().split())
a.sort(reverse=True)

ans = 0
for i in xrange(n):
    ans += (1 << i) * a[i]
print ans

