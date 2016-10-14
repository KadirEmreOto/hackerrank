#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
d1 = 0
for i in xrange(n):
    d1 += a[i][i] - a[i][-i-1]
print abs(d1)

