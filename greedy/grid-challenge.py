
T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())

    matrix = []
    for _ in xrange(N):
        matrix.append(sorted(list(raw_input())))

    for j in xrange(N):
        check = True
        for i in xrange(N-1):
            if matrix[i][j] > matrix[i+1][j]:
                check = False
                break
        if not check:
            break
    if check:
        print 'YES'
    else:
        print 'NO'



