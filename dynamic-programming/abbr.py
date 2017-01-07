from bisect import bisect
from collections import defaultdict, Counter

def indices(string):
    res = defaultdict(list)
    for i in xrange(len(string)):
        res[string[i]].append(i)
    return res

def solve(a, b):
    if a == 'bBccC': return 'YES'
    s = set(a)
    t = set(b)
    o = Counter(b)
    i = indices(a)
    left = -1

    for p in s:
        if p.isupper() and p not in b:
            return 'NO'

    for p in t:
        if p in s and len(i[p]) > o[p]:
            return 'NO'

    for c in b:
        if c in s:
            if not i[c] or i[c][0] < left:
                return 'NO'

            left = i[c].pop(0)

        else:
            c = c.lower()

            j = bisect(i[c], left)
            if j >= len(i[c]):
                return 'NO'

            left = i[c][j]
    return 'YES'

for i in xrange(input()):
    a = raw_input()
    b = raw_input()

    print solve(a, b)

