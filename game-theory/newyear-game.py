
T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().split())

    counter = [0, 0, 0]
    for i in a: counter[i%3] += 1

    if not counter[1] % 2 and not counter[2] % 2:print 'Koca'
    else:print 'Balsa'

