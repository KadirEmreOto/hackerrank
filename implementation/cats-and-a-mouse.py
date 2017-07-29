
for i in xrange(int(raw_input())):
    a, b, c = map(int, raw_input().split())
    if abs(a-c) == abs(b-c):
        print "Mouse C"
    elif abs(a-c) > abs(b-c):
        print "Cat B"
    else:
        print "Cat A"
