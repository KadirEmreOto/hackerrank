
for i in xrange(int(raw_input())):
    n = int(raw_input())
    
    if n < 38:
        print n
        
    elif n % 5 >= 3:
        print n - n % 5 + 5 
        
    else:
        print n

