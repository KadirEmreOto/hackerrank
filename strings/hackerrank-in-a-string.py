
for _ in xrange(int(raw_input())):
    string = raw_input()
    
    key = "hackerrank"
    i = 0
    
    for s in string:
        if key[i] == s:
            i += 1
        if i == len(key):
            break
            
    print 'YES' if i == len(key) else 'NO'
