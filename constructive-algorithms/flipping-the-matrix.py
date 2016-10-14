
for i in xrange(input()):
    n = int(raw_input())
    a = 0
    g = [map(int, raw_input().split()) for i in xrange(2*n)]
    for i in xrange(n):
        for j in xrange(n):
            a += max(g[i][j], g[i][2*n-j-1], g[2*n-i-1][j], g[2*n-i-1][2*n-j-1])
    print a
