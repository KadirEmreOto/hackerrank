

for _ in xrange(int(raw_input())):
    n = int(raw_input())

    i = 0
    a = 0
    while n:
        r = n & 1
        n >>= 1

        if not r:
            a += 1 << i
        i += 1
    print a

