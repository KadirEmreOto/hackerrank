#!/bin/python

import sys


N = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

p = 0.
n = 0.
z = 0.
for i in arr:
    if i > 0: p += 1
    elif i < 0: n += 1
    elif i == 0: z += 1
        
print p / N
print n / N
print z / N
