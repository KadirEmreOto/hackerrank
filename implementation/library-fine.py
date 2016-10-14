#!/bin/python

import sys


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

if m2 == m1 and y1 == y2:
    if d1 <= d2:
        print 0
    else:
        print (d1 - d2) * 15
        
elif y1 == y2:
    if m1 < m2:
        print 0
    else:
        print (m1 - m2) * 500
    
elif y1 < y2:
    print 0
else:
    print 10000
