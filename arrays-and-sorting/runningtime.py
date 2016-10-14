
def insertionSort(ar):    
    answer = 0
    for i in xrange(1, len(ar)):
        item = ar[i]
        for j in xrange(i):
            if ar[j] > item:
                answer += 1
                
    print answer

m = raw_input()
ar = map(int, raw_input().split())
insertionSort(ar)
