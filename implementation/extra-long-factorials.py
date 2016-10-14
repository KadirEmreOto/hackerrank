#!/bin/python

import sys


n = int(raw_input().strip())

r = 1
for k in xrange(1, n+1):
    r *= k
print r
