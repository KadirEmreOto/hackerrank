
n = int(raw_input())
a = raw_input()

c = 0
r = 0
for i in xrange(n):
    r += (c == -1 and a[i] == 'U')
    c += a[i] == 'U'
    c -= a[i] == 'D'

print r
