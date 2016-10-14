
g = [0, 0, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 3, 1, 2, 2, 4, 1, 3, 1, 3]

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def first(n):
    for i in xrange(2, n):
        if not n % i:
            return i

grundy = [0] * (10**6 + 5)
primes = primes(10**6 + 5)

for i in primes:
    grundy[i] = 1

for i in xrange(2, 10**6+1):
    if grundy[i]: continue

    f = first(i)
    l = grundy[f]
    r = grundy[i / f]

    grundy[i] = max(l, r) + 1

T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    array = map(int, raw_input().split())

    ans = 0
    for i in array:
        ans ^= grundy[i]
    if ans:
        print 1
    else:
        print 2

