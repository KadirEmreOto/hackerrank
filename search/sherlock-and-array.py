
t = int(raw_input().strip())

for ti in xrange(t):
    n = int(raw_input().strip())
    l = raw_input().strip()
    l = map(int, l.strip().split(' '))
    
    check = False
    s = 0
    st = sum(l)

    for i in l:
        if s > st / 2:
            break

        k = st - s - i
        if 2*s == st - i:
            print 'YES'
            check = True
            break
        s += i
    if not check:
        print 'NO'
