#!/bin/python
def partition(ar):    
    pivot = ar[0]
    left = []
    right = [pivot]
    
    for i in xrange(1, m):
        node = ar[i]
        if node < pivot:
            left.append(node)
        else:
            right.append(node)
            
    l = left + right
    print ' '.join(map(str, l))
   
    

m = int(raw_input())
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)

