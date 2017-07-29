
n = int(raw_input())
a = map(int, raw_input().split())
a.sort()

ans = float('inf')
for i in xrange(n-1):
    ans = min(ans, a[i+1] - a[i])
print ans


