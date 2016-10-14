# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import log

def solve(a, b):
    n = bin(a)[2:]
    m = bin(b)[2:]

    m = m[len(m) - len(n) : ]

    for i in xrange(len(n)):
        if n[i] != m[i]:
            break

    return int(n[:i] + '0'*(len(n) - i ), 2)


for _ in xrange(int(raw_input())):
    a, b = map(int, raw_input().split())


    print solve(a,b)

