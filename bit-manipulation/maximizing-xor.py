#!/bin/python

# Complete the function below.
import operator

def  maxXor(l, r):
    if l > r: l, r = r, l
    res = 0
    for i in xrange(l, r+1):
        for j in xrange(i, r+1):
            res = max(res, operator.xor(i, j))
    return res
    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)


