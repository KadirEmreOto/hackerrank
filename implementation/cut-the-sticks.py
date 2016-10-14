#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.sort()

while arr:
    print len(arr)
    f = arr.pop(0)
    arr = arr[arr.count(f):]
    for i in range(len(arr)):
        arr[i] -= f
        
