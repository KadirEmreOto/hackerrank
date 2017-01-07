
a = raw_input()
b = raw_input()
k = int(raw_input())

for i in xrange(min(len(a), len(b))):
    if a[i] != b[i]: break
        
r = len(a)+len(b) - 2*i
if r > k: print 'No'
elif r == k: print 'Yes'
elif k - r >= 2*i: print 'Yes'
elif not (k-r) & 1: print 'Yes'
else: print 'No'
    


