#!/bin/python
def insertionSort(ar):
    u = ar[-1]
    for i in range(len(ar)-2,-1,-1):
        check = False
        if ar[i] >= u:
            ar[i + 1] = ar[i]
        else:
            ar[i + 1] = u
            check = True
            
        for k in ar:
            print k,
        print 
        if check:break
    if not check:
        ar[0] = u
        for k in ar:
            print k,
    return ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

