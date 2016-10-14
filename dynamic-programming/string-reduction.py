from collections import Counter

T = int(raw_input())
for t in xrange(T):
    line = raw_input()
    a = [0, 0, 0]
    for i in line:
        if i == 'a':
            a[0] += 1
        elif i == 'b':
            a[1] += 1
        else:
            a[2] += 1

    while a.count(0) < 2:
        m = 0, a[0]
        for i in xrange(1, 3):
            if a[i] < m[1]:
                m = i, a[i]

        a[m[0]] += 1
        for i in xrange(3):
            if i != m[0]:
                a[i] -= 1

    print sum(a)

