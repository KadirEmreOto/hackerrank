
for _ in xrange(int(raw_input())):
    n = int(raw_input())
    a = map(int, raw_input().split())
    s = [(a[i], i) for i in xrange(n)]
    s.sort(key=lambda x: -x[0])

    ans = 0
    i = 1
    j = s[0][1]
    while j != 0:
        if s[i][1] < j:
            j = s[i][1]
            ans += 1
        i += 1

    print 'ANDY' if ans & 1 else 'BOB'

