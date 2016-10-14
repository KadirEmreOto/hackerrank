if __name__ == '__main__':
    T = int(raw_input())

    for t0 in xrange(T):
        N, K = map(int, raw_input().split())

        A = map(int, raw_input().split())
        B = map(int, raw_input().split())

        A = sorted(A)
        B = sorted(B, reverse=True)

        check = True
        for i in xrange(N):
            if A[i] + B[i] < K:
                print 'NO'
                check = False
                break

        if check:
            print 'YES'
