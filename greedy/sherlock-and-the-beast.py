#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    
    for i in range(n+1):
        l = n - i*5
        if l < 0: 
            print -1
            break
            
        if not l % 3:
            print int('5'*l + '3'*i*5)
            break
