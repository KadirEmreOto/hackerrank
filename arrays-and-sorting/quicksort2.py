#!/bin/python
def quickSort(ar):    
    pivot = ar[0]
    left = []
    right = []
    
    for i in xrange(1, len(ar)):
        node = ar[i]
        if node < pivot:
            left.append(node)
        else:
            right.append(node)
            
    if len(left) > 1:
        left = quickSort(left)
    if len(right) > 1:
        right = quickSort(right)
        
    print ' '.join(map(str, left + [pivot] + right))
    return left + [pivot] + right
    

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)

