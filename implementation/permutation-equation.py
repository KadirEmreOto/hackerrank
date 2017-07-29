
n = int(raw_input())
a = map(int, raw_input().split())
d = {}

for i in xrange(n):
    d[a[i]] = i+1
    
for i in xrange(n):
    print d[d[i+1]]
    
    
