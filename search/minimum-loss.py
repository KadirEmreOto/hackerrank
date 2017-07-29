from bisect import bisect

n = int(raw_input())
a = map(int, raw_input().split())
a = [(a[i], i) for i in xrange(n)]
s = sorted(a)

answer = float('inf')
for i in xrange(n):
    pos = bisect(s, a[i]) - 1

    for j in xrange(pos-1, -1, -1):
        if s[j][1] > i:
            answer = min(answer, a[i][0] - s[j][0])
            break

print answer
