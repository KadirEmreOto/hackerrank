#!/bin/python

import sys


n = int(raw_input().strip())
for i in xrange(1, n+1):
    print ' '*(n-i) + '#'*i
