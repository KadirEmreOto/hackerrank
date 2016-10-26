
n = int(raw_input())

a = 5
r = 0
for i in xrange(n):
    r += a / 2
    a = 3 * (a / 2)
    
print r
