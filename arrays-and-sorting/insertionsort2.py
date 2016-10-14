#!/bin/python
def insertionSort(ar):    
    for i in range(1, len(ar)):
        item = ar[i]
        for j in range(i):
            if ar[j] > item:
                ar.remove(item)
                ar.insert(j, item)
                break
        for k in ar:
            print k,
        print


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
