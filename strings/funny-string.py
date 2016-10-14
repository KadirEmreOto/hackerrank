# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
sl = string.ascii_lowercase

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    r = s[::-1]

    check = True
    for i in xrange(1, len(s)):
        s1 = s[i]
        s0 = s[i-1]
        
        r1 = r[i]
        r0 = r[i-1]
        
        sc = sl.index(s1) - sl.index(s0)
        rc = sl.index(r1) - sl.index(r0)
        if sc != rc and sc != -rc:
            check = False
            break
    if check:
        print 'Funny'
    else:
        print 'Not Funny'
            
    
    
    
    
