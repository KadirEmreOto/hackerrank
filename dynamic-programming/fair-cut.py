

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()

k = min(k, n - k)
s = (n - 2*k) / 2 + 1

t = set(xrange(s, s + k*2, 2))

answer = 0
for i in xrange(n):
    for j in xrange(n):
        if i not in t and j in t:
            answer += abs(a[j] - a[i])
print answer

