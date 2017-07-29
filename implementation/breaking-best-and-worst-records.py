
n = int(raw_input())
ar = map(int, raw_input().split())

l = m = ar[0]

a, b = 0, 0
for i in xrange(1, n):
    if ar[i] > m:
        b += 1
        m = ar[i]

    if ar[i] < l:
        a += 1
        l = ar[i]

print b,a


