#-*- coding: UTF-8 -*-
from bisect import bisect
from sys import setrecursionlimit
from math import log
setrecursionlimit(10**5)

def Solve(l, r):
    t = s[r+1] - s[l]
    if t == 0: return r - l
    #print l, r, t
    if t & 1 or l >= r: return 0

    answer = 0
    m = bisect(s, s[l]+t/2)-1
    #print '\t', t, m, s
    if s[m] == (s[l] + t/2):
        answer = 1
        answer += max(Solve(l, m-1), Solve(m, r))
    return answer


T = int(raw_input())
for t in xrange(T):
    s = [0]     # Sum Array
    n = int(raw_input())
    a = map(int, raw_input().split())
    for i in a: s.append(s[-1]+i)

#   print s[n]
    print Solve(0, n-1)

