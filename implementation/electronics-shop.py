from bisect import bisect

s, n, m = map(int, raw_input().split())
k = map(int, raw_input().split())
u = map(int, raw_input().split())

k.sort()
u.sort()

if u[0] + k[0] > s:
    print -1

else:
    a = 0
    for i in k:
        r = s - i
        if r < 0: continue
        p = bisect(u, r)
        if p == 0: continue

        a = max(a, u[p-1] + i)
    print a

