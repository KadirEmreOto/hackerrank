
import sys, resource
sys.setrecursionlimit(10**5 + 4)
resource.setrlimit(resource.RLIMIT_STACK, (65532000, 65532000))

def Solve(n, pre):
    if n == -1: return 0
    if pre != arr[n+1]:
        if not dp[n][1]:
            dp[n][1]=max(Solve(n-1,arr[n])+abs(arr[n]-pre), Solve(n-1,1)+abs(1-pre))
        return dp[n][1]

    else:
        if not dp[n][0]:
            dp[n][0]=max(Solve(n-1,arr[n])+abs(arr[n]-pre), Solve(n-1,1)+abs(1-pre))
        return dp[n][0]

T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())

    arr = map(int, raw_input().split())
    if set(arr) == {1}: print 0; continue
    if N == 1: print 0; continue
    dp = [[0, 0] for i in xrange(N)]

    print max(Solve(N-2,arr[N-1]), Solve(N-2,1))

