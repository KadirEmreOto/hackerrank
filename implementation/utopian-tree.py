#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    init = 1
    
    for i in range(1, n+1):
        if i % 2: init *= 2
        else: init += 1

    print init
        
