from random import shuffle

for q in xrange(int(input())):
    n = int(raw_input())
    a = map(int, raw_input().split())
    a.sort(), a.append(float('inf'))

    r = 0
    k = 0
    for i in xrange(n):
        if a[i-1] != a[i]:
            k = (n - i)
        r += (float(n)+1) / (k+1)
    print '%0.2f'%(r)

