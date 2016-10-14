# Enter your code here. Read input from STDIN. Print output to STDOUT

def insertionSort(ar):    
    answer = 0
    for i in xrange(1, len(ar)):
        item = ar[i]
        for j in xrange(i):
            if ar[j] > item:
                answer += 1
                
    return answer

def partition(ar, s=0, f=None):
    global q
    if f is None: f = m-1
    if f - s < 1: return
    pivot = ar[f]
    i, j = s, s
    while j < f:
        if ar[j] < pivot:
            ar[i], ar[j] = ar[j], ar[i]
            i += 1
            q += 1

        j += 1
    q += 1
    ar[i], ar[f] = ar[f], ar[i]
    
    partition(ar, s, i-1)
    partition(ar, i+1, f)
        

m = int(raw_input())
ar = map(int, map(int, raw_input().split()))

q = 0
i = insertionSort(ar) 
partition(ar)
print i - q
