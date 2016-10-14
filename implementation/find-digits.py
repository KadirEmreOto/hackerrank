#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    
    count = 0
    for i in str(n):
        i = int(i)
        if i != 0 and not n % i:
            count += 1
    print count

