#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)] # 6 2 2  3  

    r = n / c 
    k = r
    
    while k >= m:
        ek = k / m
        r += ek
        k %= m

        k += ek
    print r
