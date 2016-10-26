from math import factorial

n = long(raw_input())
if not n: print 1; quit()

b = bin(n)[2:]
c = b.count('0')
print 1<<c
