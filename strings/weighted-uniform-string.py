from string import ascii_lowercase
from collections import defaultdict

text = raw_input() + '#'
n = len(text)
s = set()
c = defaultdict(int)

i = 0
while i < n :
    t = text[i]

    for j in xrange(n - i):
        #print i, j, n
        if t == text[i+j]:
            if t == '#': i += 1; break
            p = (ascii_lowercase.index(t) + 1) * (j+1)
            s.add(p)

        else:
            i += j
            break
            
for i in xrange(int(raw_input())):
    print 'Yes' if int(raw_input()) in s else 'No'

