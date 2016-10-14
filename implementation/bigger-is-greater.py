# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

T = int(raw_input())

for t0 in xrange(T):
    text = raw_input()
    array = list(text)

    visited = []
    for i in xrange(len(array)-1, 0, -1):
        visited.append(array[i])
        if array[i] > array[i-1]:
            c = max(visited)
            for k in visited:
                if c > k > array[i-1]:
                    c = k
            visited.remove(c)
            visited.append(array[i-1])
            array[i-1] = c
            visited.sort()
            array[i:] = visited
            break
    
    answer = ''.join(array)
    if answer == text:
        print 'no answer'
    else:
        print answer
            
        
            
