from collections import Counter

for i in xrange(input()):
    n = int(raw_input())
    s = raw_input()
    c = Counter(s)
    if '_' in c: del c['_']
    if 1 in c.values():
        print 'NO'
    else:
        if '_' in s: 
            print 'YES'
        else:
            check = True
            for i in xrange(n):
                if (i-1 >= 0 and s[i-1] == s[i]) or (i+1 < n and s[i+1] == s[i]):
                    continue
                check = False
                break
            print 'YES' if check else 'NO'
                


