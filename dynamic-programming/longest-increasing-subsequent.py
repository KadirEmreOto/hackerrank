import sys

def readline():
    return sys.stdin.readline().strip()

def BinarySearch(array, item, start, end):
    if(start > end): return start

    mid = (start + end) // 2

    if item == array[start]: return start
    if item == array[mid]  : return mid
    if item == array[end]  : return end

    if (item < array[mid]): return BinarySearch(array, item, start, mid-1)

    return BinarySearch(array, item, mid+1, end)

def Solve(A):
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
            k = BinarySearch(c, A[i], 1,sz)
            c[k] = A[i]
            dp[i] = k

    return max(dp)

if __name__ == "__main__":
    N = int(readline())

    array = []
    for i in xrange(N):
        array.append(int(readline()))

    result = Solve(array)
    print result
