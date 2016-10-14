from bisect import bisect

n, d = map(int, raw_input().split())
a = map(int, raw_input().split())

answer = 0
for it in a:
    i = bisect(a, it + d)
    if a[i - 1] != it + d: continue

    i = bisect(a, it + 2 * d)
    if a[i - 1] != it + 2 * d: continue

    answer += 1

print answer

