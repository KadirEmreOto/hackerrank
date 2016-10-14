# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

string = raw_input()
counter = Counter(string)

values = counter.values()
counter = Counter(values)


if len(counter) > 2:
    print 'NO'

elif len(counter) == 2:
    if counter.values()[0] == 1 or counter.values()[1] == 1:
        print 'YES'
    else:
        print 'NO'

elif len(counter) < 2:
    print 'YES'
    

