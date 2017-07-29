from sys import setrecursionlimit; setrecursionlimit(10**6 + 5)
import resource; resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
from collections import defaultdict

def Solve(i=0, sep=[]):
    if i in visited:
        return
    
    visited.add(i)
    if i == len(attempt):
        return sep

    for word in d[attempt[i]]:
        if word == attempt[i:i+len(word)]:
            t = Solve(i + len(word), sep+[i])
            if t is not None:
                return t

for _ in xrange(int(raw_input())):
    d = defaultdict(set)
    n = int(raw_input())

    words = raw_input().split()

    for word in words:
        d[word[0]].add(word)

    visited = set()
    attempt = raw_input()
    ans = Solve()

    if ans is None:
        print "WRONG PASSWORD"

    else:
        for i in xrange(len(ans) - 1):
            print attempt[ans[i]: ans[i+1]],
        print attempt[ans[-1]:]


