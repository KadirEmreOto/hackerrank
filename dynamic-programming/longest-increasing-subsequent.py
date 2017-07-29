from bisect import bisect_left

def LIS(A):
    length = len(A)

    dp = [1]*length
    c  = [0]*length
    c[1] = A[0]

    sz = 1
    for i in xrange(1, length):
        if(A[i] < c[1]):
            c[1] = A[i]
            dp[i] = 1

        elif(A[i] > c[sz]):
            c[sz + 1] = A[i]
            dp[i] = sz + 1
            sz += 1

        else:
            k = bisect_left(c, A[i], 1,sz)
            c[k] = A[i]
            dp[i] = k

    return max(dp)

if __name__ == "__main__":
    n = int(raw_input())
    a = [int(raw_input()) for i in xrange(n)]

    print LIS(a)

