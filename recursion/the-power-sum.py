
x = int(raw_input())
n = int(raw_input())
a = [i ** n for i in xrange(1, int(x ** (1./n)) + 2)]

d = [0] * (x + 1)
d[0] = 1

for k in a:
    for i in xrange(x, -1, -1):
        if i + k <= x and d[i] != 0:
            d[i + k] += d[i]

print d[-1]

