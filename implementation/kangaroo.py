

a, x, b, y = map(int, raw_input().split())

if a > b:
    a, b = b, a
    x, y = y, x

if x == y and not (b - a) % x:
    print 'YES'
elif x == y:
    print 'NO'
else:
    if (b - a) % (x - y): print 'NO'
    else:
        c = (b - a) / (x - y)
        if a + c*x >= b:print 'YES'
        else: print 'NO'
    


