
n, k = map(int, raw_input().split())
x, y = map(int, raw_input().split())

obstacle = set(tuple(map(int, raw_input().split())) for i in xrange(k))

answer = 0
for i in xrange(-1, 2):
    for j in xrange(-1, 2):
        if i == j == 0: continue

        u, v = x+i, y+j
        while 0 < u <= n and 0 < v <= n and  (u, v) not in obstacle:
            u += i
            v += j
            answer += 1
print answer


