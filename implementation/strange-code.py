from bisect import bisect_left

a = []
a.append(1)
for i in xrange(45):
    a.append(a[-1] +  3 * (1<<i))


t = int(raw_input());
i = bisect_left(a, t)
if a[i] != t: i -= 1

print (1<<i) * 3 - (t - a[i])

