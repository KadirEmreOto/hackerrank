

T = int(raw_input())

for t0 in xrange(T):
    N , M = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    res = [1] + [0]*M

    for i in arr:
        for r in xrange(len(res)):
            check = res[r]
            if check:
                if r + i < M + 1:
                    res[r+i] = 1

    for i in xrange(M, -1, -1):
        if res[i]:
            print i
            break




