# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())

for t0 in xrange(T):
    A = set(raw_input())
    B = set(raw_input())
    
    check = False
    for i in A:
        if i in B:
            check = True
            break
    if check:
        print 'YES'
    else: 
        print 'NO'
