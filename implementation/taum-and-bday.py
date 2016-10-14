#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    if x + z < y:
        y = x + z
        
    if y + z < x:
        x = y + z
    print b*x + w*y

