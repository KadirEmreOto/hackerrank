# Enter your code here. Read input from STDIN. Print output to STDOUT

def partition(ar, s=0, f=None):
    if f is None: f = m-1
    if f - s < 1: return
    pivot = ar[f]
    i, j = s, s
    while j < f:
        if ar[j] < pivot:
            ar[i], ar[j] = ar[j], ar[i]
            i += 1

        j += 1
        
    ar[i], ar[f] = ar[f], ar[i]
    print ' '.join(map(str, ar))
    
    partition(ar, s, i-1)
    partition(ar, i+1, f)
        
m = int(raw_input())
ar = map(int, map(int, raw_input().split()))
partition(ar)
