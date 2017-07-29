from bisect import bisect

def sieve(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

p = sieve(10**5 + 10)

for i in xrange(input()):
    n = int(raw_input())
    t = bisect(p, n)

    print 'Alice' if t & 1 else 'Bob'


