# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial as fac

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def Count(N):
    count = 0
    for four in xrange(N / 4 + 1):
        one = N - 4*four
        count += fac(one+four) / (fac(one)*fac(four))
    return count

T = int(raw_input())
for t0 in xrange(T):
    N = int(raw_input())
    if N < 4:
        print 0
    else:
        print len(primes(Count(N)+1))
